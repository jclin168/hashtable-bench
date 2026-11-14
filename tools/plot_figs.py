#!/usr/bin/env python3
"""Render README line charts (PNG) from benchmark CSVs, without Jupyter.

Same look as tools/analyze_results.ipynb (log x and y, 8x6 inches, 300 dpi,
legend on the right), one line per map/hash pair. A run of zeros (timeout)
ends a line.

Usage:
  python3 plot_figs.py --time-csv DIR [--mem-csv DIR] --platform NAME --out DIR

Figure names: <key,value>,<metric>.png, e.g.
  <mask_split_bits_uint64_t,uint64_t>,avg_hit_find_with_rehash.png
"""
import argparse
import colorsys
import itertools
import os
import re

import matplotlib
matplotlib.use("Agg")
import matplotlib.pyplot as plt
import matplotlib.ticker as plticker
import pandas as pd

# metric name -> (csv column, y label, log y)
TIME_METRICS = {
    "avg_insert_time_with_reserve": ("avg_construct_time_with_reserve_ns", "ns", True),
    "avg_insert_time_without_reserve": ("avg_construct_time_without_reserve_ns", "ns", True),
    "avg_erase_insert_time": ("avg_erase_insert_ns", "ns", True),
    "avg_hit_find_without_rehash": ("avg_hit_default_load_factor_lookup_ns", "ns", True),
    "avg_miss_find_without_rehash": ("avg_miss_default_load_factor_lookup_ns", "ns", True),
    "avg_hit_find_with_rehash": ("avg_hit_large_max_load_factor_lookup_ns", "ns", True),
    "avg_miss_find_with_rehash": ("avg_miss_large_max_load_factor_lookup_ns", "ns", True),
    "avg_iterate": ("avg_iterate_ns", "ns", True),
}
# "heap_bytes_per_element" is final_default_load_factor_size_mb * 2^20 / element_num
MEM_METRICS = {
    "heap_bytes_per_element": ("final_default_load_factor_size_mb", "heap bytes per element", False),
    "load_factor": ("no_rehash_load_factor", "load factor", False),
}
PATTERN = re.compile(r"(.+)__(.+)__(.+)__(.+)\.csv")


def load(csv_dir):
    # {(key, value): {"map,hash": DataFrame}}
    out = {}
    for name in sorted(os.listdir(csv_dir)):
        m = PATTERN.fullmatch(name)
        if not m:
            continue
        map_name, hash_name, key, value = m.groups()
        df = pd.read_csv(os.path.join(csv_dir, name))
        df = df.rename(columns=lambda c: c.strip())
        out.setdefault((key, value), {})[map_name + "," + hash_name] = df
    return out


def styles(labels):
    labels = sorted(labels)
    colors = {}
    for i, label in enumerate(labels):
        colors[label] = colorsys.hsv_to_rgb(i / len(labels), 0.75, 0.85)
    markers = dict(zip(labels, itertools.cycle("^os<p*>v+xD")))
    return colors, markers


def plot(title, series, ylabel, log_y, path, colors, markers):
    fig, ax = plt.subplots(figsize=(8, 6), dpi=300)
    fig.suptitle(title, fontsize="small")
    for label in sorted(series):
        x, y = series[label]
        n = 0
        while n < len(y) and y[n] > 0.0:
            n += 1
        if n == 0:
            continue
        ax.plot(x[:n], y[:n], label=label, color=colors[label],
                marker=markers[label], markersize=2.5, linewidth=1.0)
    ax.set_xscale("log")
    ax.set_xlabel("element num")
    ax.set_ylabel(ylabel)
    if log_y:
        ax.set_yscale("log")
        ax.yaxis.set_minor_locator(plticker.LogLocator(subs=[1.0, 2.0, 4.0, 6.0]))
        ax.yaxis.set_minor_formatter(plticker.FormatStrFormatter("%.0f"))
    else:
        ax.set_ylim(bottom=0)
    ax.grid(True, which="major", linewidth=0.3)
    box = ax.get_position()
    ax.set_position([box.x0, box.y0, box.width * 0.8, box.height])
    handles, labels = ax.get_legend_handles_labels()
    fig.legend(handles, labels, loc="center right", fontsize="xx-small")
    fig.savefig(path, transparent=False, facecolor="white")
    plt.close(fig)


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("--time-csv", required=True)
    ap.add_argument("--mem-csv")
    ap.add_argument("--platform", required=True)
    ap.add_argument("--out", required=True)
    args = ap.parse_args()
    os.makedirs(args.out, exist_ok=True)

    jobs = [(load(args.time_csv), TIME_METRICS)]
    if args.mem_csv:
        jobs.append((load(args.mem_csv), MEM_METRICS))
    labels = {l for data, _ in jobs for maps in data.values() for l in maps}
    colors, markers = styles(labels)

    count = 0
    for data, metrics in jobs:
        for (key, value), maps in sorted(data.items()):
            for metric, (col, ylabel, log_y) in metrics.items():
                series = {l: (df["element_num"].to_numpy(), df[col].to_numpy())
                          for l, df in maps.items() if col in df}
                if metric == "heap_bytes_per_element":
                    series = {l: (x, y * 1048576.0 / x) for l, (x, y) in series.items()}
                if not series:
                    continue
                name = "<%s,%s>,%s" % (key, value, metric)
                plot("%s %s" % (args.platform, name), series, ylabel, log_y,
                     os.path.join(args.out, name + ".png"), colors, markers)
                count += 1
    print("wrote %d figures to %s" % (count, args.out))


if __name__ == "__main__":
    main()
