# Apple M2, November 2026, std::hash

Apple M2 (MacBook Air, 16 GiB), macOS 27.2, Apple clang 21.0.0 (libc++), CMake `Release` with `-mcpu=native`, seed 42, one
benchmark at a time, no core pinning (macOS has none). sflat is jclin168/sflat_hash_map main (aaded6f).

- `time/csv`, `logs/time_*.log`: timing of the six maps. `build.sh` builds, `run.sh` runs (time pass, then memory pass).
  `logs/progress.log` has the start and end of every run and the effective clock before and after each map
  (`clk`, from `tools/clk.cpp`; 3.47 to 3.50 iterations per ns throughout, the first sample of a probe can be lower).
- `mem/csv`, `logs/mem_*.log`: heap memory (count_allocator build, `-DBENCH_HEAP_MEMORY_SIZE=ON`).
- `time-first-run/`: the first timing run of sflat. It overlapped with a `pip install` and had two spurious 120 s lookup
  timeouts at 600,000 elements, so sflat was run again alone (`time-rerun/`, 19 min instead of 44). `time/csv` and
  `logs/time_sflat_flat_hash_map.log` hold the rerun.
- `summary.md`: markdown tables (`python3 tools/summarize_csv.py results/m2-202611/time/csv results/m2-202611/mem/csv`).
- Figures: `results/show/m2-202611` (`tools/plot_figs.py --time-csv results/m2-202611/time/csv --mem-csv results/m2-202611/mem/csv --platform "Apple M2" --out results/show/m2-202611`).
- The write-up is [`README_MAC.md`](../../README_MAC.md).
