#!/bin/bash
# Seed 42; each binary pinned to core 2 (CPUs 0,2 online). Timing builds first, then the count_allocator builds.
cd "$(dirname "$0")/../.."
R=results/i5-3230M-202611
MAPS="sflat_flat_hash_map ankerl_unordered_map absl_flat_hash_map boost_unordered_flat_map emhash_map8 std_unordered_map"
for kind in time mem; do
  for m in $MAPS; do
    exe=build-$kind/bench_${m}__std_hash
    echo "$(date -Is) start $kind $m"
    /usr/bin/time -v taskset -c 2 $exe 42 $R/$kind/csv/ > $R/logs/${kind}_${m}.log 2>&1
    echo "$(date -Is) done $kind $m exit $?"
  done
done
echo "$(date -Is) ALL DONE"
