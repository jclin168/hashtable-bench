#!/bin/bash
# Seed 42, one benchmark at a time, nothing else running. macOS has no core pinning; caffeinate keeps the Mac awake.
cd /Users/jclin/claude/hbench_work/src
R=results/m2-202611
MAPS="sflat_flat_hash_map boost_unordered_flat_map ankerl_unordered_map absl_flat_hash_map emhash_map8 std_unordered_map"
log() { echo "$(date +%Y-%m-%dT%H:%M:%S%z) $*" >> $R/logs/progress.log; }
for kind in time mem; do
  for m in $MAPS; do
    if [ "$kind" = time ]; then log "clock before $m: $($R/clk)"; fi
    log "start $kind $m"
    /usr/bin/time -l build-$kind/bench_${m}__std_hash 42 $R/$kind/csv/ > $R/logs/${kind}_${m}.log 2>&1
    log "done $kind $m exit $?"
    if [ "$kind" = time ]; then log "clock after $m: $($R/clk)"; fi
  done
done
log "ALL DONE"
