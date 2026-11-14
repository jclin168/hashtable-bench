#!/bin/bash
# Timing rerun with both cores on the performance governor and turbo off (the first run was at a clock that
# changed with the load on the other core). Seed 42, core 2, one benchmark at a time; nothing else may run.
# $R/clk logs the effective clock before and after each map (iterations/ns of a dependent add loop; ~1.3 is normal).
cd "$(dirname "$0")/../.."
R=results/i5-3230M-202611
log() { echo "$(date -Is) $*"; }
clk() { log "clock $1: $(taskset -c 2 $R/clk)"; }
run() {  # label exe csv_dir logfile
  clk "before $1"; log "start time $1"
  /usr/bin/time -v taskset -c 2 $2 42 $3 > $4 2>&1; log "done time $1 exit $?"; clk "after $1"
}
for m in sflat_flat_hash_map boost_unordered_flat_map ankerl_unordered_map absl_flat_hash_map emhash_map8 std_unordered_map; do
  run $m build-time/bench_${m}__std_hash $R/time/csv/ $R/logs/time_${m}.log
done
run sflat_d0677db build-time-base/bench_sflat_flat_hash_map__std_hash $R/sflat-d0677db/time/csv/ $R/sflat-d0677db/time/time_sflat_flat_hash_map.log
log "ALL TIME DONE"
