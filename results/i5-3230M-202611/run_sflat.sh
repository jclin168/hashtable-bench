#!/bin/bash
# Rerun of sflat only (sflat at the perf-slow-spots commit b4380ed), same conditions as run_time.sh/run.sh:
# both cores on performance, turbo off, seed 42, core 2, one benchmark at a time. Timing first, then count_allocator memory.
# The previous sflat results (aaded6f) are kept in sflat-aaded6f/.
cd "$(dirname "$0")/../.."
R=results/i5-3230M-202611
m=sflat_flat_hash_map
log() { echo "$(date -Is) $*"; }
clk() { log "clock $1: $(taskset -c 2 $R/clk)"; }
for kind in time mem; do
  clk "before $kind"; log "start $kind $m"
  /usr/bin/time -v taskset -c 2 build-$kind/bench_${m}__std_hash 42 $R/$kind/csv/ > $R/logs/${kind}_${m}.log 2>&1
  log "done $kind $m exit $?"; clk "after $kind"
done
log "ALL DONE"
