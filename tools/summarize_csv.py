"""Summarize benchmark CSVs into markdown tables.

Usage: python3 summarize_csv.py time_csv_dir [mem_csv_dir] > summary.md

File names follow the benchmark's pattern: {map}__{hash}__{dataset}__{value}.csv
Timing tables show ns per operation at a few sizes (closest available size);
memory tables show the heap bytes per element measured by count_allocator.
"""
import csv
import os
import sys
from collections import defaultdict

DATASETS = [
    "mask_split_bits_uint64_t__uint64_t",
    "uniform_uint64_t__uint64_t",
    "mask_high_bits_uint64_t__uint64_t",
    "mask_low_bits_uint64_t__uint64_t",
    "mask_split_bits_uint64_t__56bytes_payload",
    "small_string_max_12__uint64_t",
    "small_string_fix_12__uint64_t",
    "mid_string_max_24__uint64_t",
    "mid_string_fix_24__uint64_t",
    "long_string_max_64__uint64_t",
    "long_string_fix_64__uint64_t",
]

OPS = [
    ("avg_construct_time_with_reserve_ns", "insert (reserve)"),
    ("avg_construct_time_without_reserve_ns", "insert (no reserve)"),
    ("avg_erase_insert_ns", "erase+insert"),
    ("avg_hit_default_load_factor_lookup_ns", "find hit"),
    ("avg_miss_default_load_factor_lookup_ns", "find miss"),
    ("avg_50%_hit_default_load_factor_lookup_ns", "find 50%"),
    ("avg_hit_large_max_load_factor_lookup_ns", "find hit (mlf 0.9)"),
    ("avg_miss_large_max_load_factor_lookup_ns", "find miss (mlf 0.9)"),
    ("avg_iterate_ns", "iterate"),
]

TIME_SIZES = [1024, 100000, 1200000, 10000000]
MEM_SIZES = [1638, 104857, 1258291, 10000000]


def load(csv_dir):
    # data[dataset][map] = {element_num: row}
    data = defaultdict(dict)
    for name in sorted(os.listdir(csv_dir)):
        if not name.endswith(".csv"):
            continue
        parts = name[:-4].split("__")
        if len(parts) != 4:
            continue
        map_name, _hash_name, ds, value = parts
        rows = {}
        with open(os.path.join(csv_dir, name)) as f:
            for row in csv.DictReader(f):
                rows[int(row["element_num"])] = row
        data[ds + "__" + value][map_name] = rows
    return data


def closest(rows, size):
    if not rows:
        return None
    k = min(rows, key=lambda n: abs(n - size))
    return k if abs(k - size) <= size * 0.25 else None


def fmt(v):
    if v is None:
        return "-"
    return "%.1f" % v if v < 100 else "%.0f" % v


def time_tables(data):
    out = []
    for ds in DATASETS:
        maps = data.get(ds)
        if not maps:
            continue
        out.append("### %s\n" % ds)
        for size in TIME_SIZES:
            names = list(maps)
            hdr = "| n=%s ns/op | " % format(size, ",") + " | ".join(names) + " |"
            out.append(hdr)
            out.append("|" + "---|" * (len(names) + 1))
            for col, label in OPS:
                vals = []
                for m in names:
                    k = closest(maps[m], size)
                    vals.append(float(maps[m][k][col]) if k is not None else None)
                present = [v for v in vals if v is not None and v > 0]
                best = min(present) if present else None
                cells = []
                for v in vals:
                    s = fmt(v)
                    if v is not None and v == best:
                        s = "**%s**" % s
                    cells.append(s)
                out.append("| %s | %s |" % (label, " | ".join(cells)))
            out.append("")
    return "\n".join(out)


def mem_tables(data):
    out = []
    for ds in DATASETS:
        maps = data.get(ds)
        if not maps:
            continue
        names = list(maps)
        out.append("### %s\n" % ds)
        out.append("Heap bytes per element after inserting n keys with reserve(n) "
                   "(final / peak), and load factor.\n")
        out.append("| n | " + " | ".join(names) + " |")
        out.append("|" + "---|" * (len(names) + 1))
        for size in MEM_SIZES:
            cells = []
            for m in names:
                k = closest(maps[m], size)
                if k is None:
                    cells.append("-")
                    continue
                r = maps[m][k]
                final_b = float(r["final_default_load_factor_size_mb"]) * 1024 * 1024 / k
                peak_b = float(r["peak_default_load_factor_size_mb"]) * 1024 * 1024 / k
                cells.append("%.1f / %.1f (lf %.2f)" % (final_b, peak_b,
                                                       float(r["no_rehash_load_factor"])))
            out.append("| %s | %s |" % (format(size, ","), " | ".join(cells)))
        out.append("")
        out.append("Total MiB at the largest size (final, default max_load_factor / "
                   "after max_load_factor(0.9)+rehash):\n")
        out.append("| map | final MiB | peak MiB | final MiB (mlf 0.9) | lf | lf (mlf 0.9) |")
        out.append("|---|---|---|---|---|---|")
        for m in names:
            rows = maps[m]
            if not rows:
                continue
            k = max(rows)
            r = rows[k]
            out.append("| %s | %.1f | %.1f | %.1f | %.3f | %.3f |" % (
                m, float(r["final_default_load_factor_size_mb"]),
                float(r["peak_default_load_factor_size_mb"]),
                float(r["final_large_load_factor_size_mb"]),
                float(r["no_rehash_load_factor"]), float(r["with_rehash_load_factor"])))
        out.append("")
    return "\n".join(out)


def main():
    if len(sys.argv) < 2:
        print(__doc__)
        return
    print("## Throughput\n")
    print(time_tables(load(sys.argv[1])))
    if len(sys.argv) > 2:
        print("## Heap memory\n")
        print(mem_tables(load(sys.argv[2])))


if __name__ == "__main__":
    main()
