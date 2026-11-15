#!/bin/bash
set -e
cd /Users/jclin/claude/hbench_work/src
MAPS="sflat_flat_hash_map ankerl_unordered_map absl_flat_hash_map boost_unordered_flat_map emhash_map8 std_unordered_map"
T=""; for m in $MAPS; do T="$T bench_${m}__std_hash"; done
cmake -S . -B build-time -DCMAKE_BUILD_TYPE=Release -DCMAKE_POLICY_VERSION_MINIMUM=3.5 -DCMAKE_CXX_FLAGS=-Wno-missing-template-arg-list-after-template-kw > /tmp/cm_time.log 2>&1
cmake -S . -B build-mem -DCMAKE_BUILD_TYPE=Release -DCMAKE_POLICY_VERSION_MINIMUM=3.5 -DCMAKE_CXX_FLAGS=-Wno-missing-template-arg-list-after-template-kw -DBENCH_HEAP_MEMORY_SIZE=ON > /tmp/cm_mem.log 2>&1
cmake --build build-time -j8 --target $T 2>&1 | tail -5
cmake --build build-mem -j8 --target $T 2>&1 | tail -5
ls build-time build-mem | grep bench_
