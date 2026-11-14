# i5-3230M, November 2026, std::hash

Intel Core i5-3230M, CPUs 0 and 2 online, GCC 15.2, `-O3 -march=native`, seed 42, one benchmark at a time on core 2.

- `time/csv`, `logs/time_*.log`, `logs/time_progress.log`: timing of the six maps, from `run_time.sh`. Both cores on the
  `performance` governor, turbo off; `logs/time_progress.log` has the effective clock before and after each map.
- `mem/csv`, `logs/mem_*.log`: heap memory (count_allocator build), from `run.sh`. `run.sh` also ran a first timing pass
  with the `powersave` governor, in which the clock of core 2 followed the load of core 0; that timing is not used, `run_time.sh` replaced it.
- `sflat-d0677db/`: sflat before the erase thresholds of jclin168/sflat_hash_map#29 (timing and memory); `time/csv` is
  sflat main (aaded6f), so the two directories compare the change.
- `summary.md`: markdown tables (`python3 tools/summarize_csv.py results/i5-3230M-202611/time/csv results/i5-3230M-202611/mem/csv`).
- Figures: `results/show/i5-3230M-202611` (`tools/plot_figs.py`).
