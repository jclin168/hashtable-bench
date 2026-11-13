#!/bin/bash
# sflat only, timing build: used 3/8 + tombstones 1/16 (sflat 90aaaef) against d0677db, rerun back to back.
# Starts after run.sh has finished. Seed 42, core 2.
cd "$(dirname "$0")/../.."
R=results/i5-3230M-202611
until grep -q "ALL DONE" $R/logs/progress.log; do sleep 30; done
for v in new:build-time-thresh base:build-time; do
  echo "$(date -Is) start thresh ${v%%:*}"
  /usr/bin/time -v taskset -c 2 ${v##*:}/bench_sflat_flat_hash_map__std_hash 42 $R/thresh/${v%%:*}/csv/ > $R/logs/thresh_${v%%:*}.log 2>&1
  echo "$(date -Is) done thresh ${v%%:*} exit $?"
done
echo "$(date -Is) THRESH DONE"
