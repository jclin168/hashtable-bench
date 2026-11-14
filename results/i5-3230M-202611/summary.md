## Throughput

### mask_split_bits_uint64_t__uint64_t

| n=1,024 ns/op | absl::flat_hash_map | ankerl::unordered_dense_map | boost::unordered_flat_map | emhash::hash_map8 | sflat::flat_hash_map | std::unordered_map |
|---|---|---|---|---|---|---|
| insert (reserve) | 387 | 14.5 | **9.0** | 475 | 10.9 | 65.5 |
| insert (no reserve) | 505 | **26.6** | 28.9 | 777 | 35.1 | 101 |
| erase+insert | 498 | 18.0 | **10.2** | 1953 | 43.7 | 62.4 |
| find hit | 329 | 6.7 | **6.6** | 459 | 6.9 | 17.7 |
| find miss | 166 | 5.8 | **4.8** | 679 | 7.0 | 25.0 |
| find 50% | 266 | 6.1 | **5.6** | 557 | 6.6 | 21.7 |
| find hit (mlf 0.9) | 328 | 7.2 | **6.7** | 456 | 6.9 | 17.8 |
| find miss (mlf 0.9) | 169 | 6.6 | **4.8** | 675 | 7.5 | 25.0 |
| iterate | 3.7 | **0.8** | 3.0 | 0.8 | 4.0 | 2.1 |

| n=100,000 ns/op | absl::flat_hash_map | ankerl::unordered_dense_map | boost::unordered_flat_map | emhash::hash_map8 | sflat::flat_hash_map | std::unordered_map |
|---|---|---|---|---|---|---|
| insert (reserve) | 0.0 | 21.5 | **14.6** | 0.0 | 16.6 | 119 |
| insert (no reserve) | 0.0 | 36.3 | **27.8** | 0.0 | 31.4 | 185 |
| erase+insert | 0.0 | 76.6 | **68.5** | 0.0 | 81.6 | 225 |
| find hit | 0.0 | 22.3 | **15.9** | 0.0 | 18.3 | 65.8 |
| find miss | 0.0 | 10.9 | **8.4** | 0.0 | 10.0 | 82.5 |
| find 50% | 0.0 | 22.1 | **20.1** | 0.0 | 21.1 | 96.0 |
| find hit (mlf 0.9) | 0.0 | 20.6 | 15.7 | 0.0 | **14.6** | 65.8 |
| find miss (mlf 0.9) | 0.0 | 10.3 | **8.4** | 0.0 | 9.7 | 81.5 |
| iterate | 0.0 | **0.8** | 2.7 | 0.0 | 3.9 | 9.9 |

| n=1,200,000 ns/op | absl::flat_hash_map | ankerl::unordered_dense_map | boost::unordered_flat_map | emhash::hash_map8 | sflat::flat_hash_map | std::unordered_map |
|---|---|---|---|---|---|---|
| insert (reserve) | 0.0 | 99.0 | 63.1 | 0.0 | **29.8** | 198 |
| insert (no reserve) | 0.0 | 105 | 78.3 | 0.0 | **50.0** | 345 |
| erase+insert | 0.0 | 194 | **131** | 0.0 | 133 | 367 |
| find hit | 0.0 | 45.0 | 32.9 | 0.0 | **28.7** | 111 |
| find miss | 0.0 | 25.4 | **15.0** | 0.0 | 15.7 | 147 |
| find 50% | 0.0 | 44.4 | 33.6 | 0.0 | **31.2** | 173 |
| find hit (mlf 0.9) | 0.0 | 46.4 | 36.4 | 0.0 | **29.0** | 112 |
| find miss (mlf 0.9) | 0.0 | 26.7 | 16.5 | 0.0 | **16.0** | 147 |
| iterate | 0.0 | **0.8** | 3.9 | 0.0 | 3.9 | 31.4 |

| n=10,000,000 ns/op | absl::flat_hash_map | ankerl::unordered_dense_map | boost::unordered_flat_map | emhash::hash_map8 | sflat::flat_hash_map | std::unordered_map |
|---|---|---|---|---|---|---|
| insert (reserve) | 0.0 | 142 | 130 | 0.0 | **45.3** | 236 |
| insert (no reserve) | 0.0 | 182 | 136 | 0.0 | **62.5** | 404 |
| erase+insert | 0.0 | 0.0 | 185 | 0.0 | **163** | 423 |
| find hit | 0.0 | 52.5 | 42.5 | 0.0 | **41.0** | 128 |
| find miss | 0.0 | 32.8 | **26.1** | 0.0 | 29.8 | 163 |
| find 50% | 0.0 | 50.2 | **43.6** | 0.0 | 44.8 | 205 |
| find hit (mlf 0.9) | 0.0 | 52.7 | 47.1 | 0.0 | **41.6** | 129 |
| find miss (mlf 0.9) | 0.0 | 32.2 | **25.5** | 0.0 | 30.2 | 161 |
| iterate | 0.0 | **0.8** | 3.7 | 0.0 | 3.9 | 39.0 |

### uniform_uint64_t__uint64_t

| n=1,024 ns/op | absl::flat_hash_map | ankerl::unordered_dense_map | boost::unordered_flat_map | emhash::hash_map8 | sflat::flat_hash_map | std::unordered_map |
|---|---|---|---|---|---|---|
| insert (reserve) | 13.3 | 15.1 | **9.9** | 12.7 | 12.1 | 70.0 |
| insert (no reserve) | 28.0 | **26.0** | 29.4 | 30.2 | 37.5 | 93.8 |
| erase+insert | 30.6 | 19.1 | **10.3** | 22.6 | 43.7 | 62.5 |
| find hit | 6.4 | 6.6 | 6.7 | **3.9** | 7.1 | 19.3 |
| find miss | 5.4 | 5.7 | 5.6 | **3.2** | 7.5 | 25.3 |
| find 50% | 5.8 | 5.9 | 5.5 | **3.6** | 6.6 | 22.8 |
| find hit (mlf 0.9) | 6.4 | 6.7 | 6.7 | **4.0** | 7.1 | 19.2 |
| find miss (mlf 0.9) | 5.4 | 5.7 | 4.9 | **3.2** | 7.3 | 25.3 |
| iterate | 3.3 | **0.8** | 3.2 | 0.8 | 3.9 | 2.1 |

| n=100,000 ns/op | absl::flat_hash_map | ankerl::unordered_dense_map | boost::unordered_flat_map | emhash::hash_map8 | sflat::flat_hash_map | std::unordered_map |
|---|---|---|---|---|---|---|
| insert (reserve) | 21.8 | 20.1 | **14.9** | 36.1 | 16.3 | 132 |
| insert (no reserve) | 36.0 | 30.6 | **27.9** | 49.2 | 31.5 | 188 |
| erase+insert | 88.3 | 78.5 | **69.5** | 81.4 | 83.1 | 220 |
| find hit | **13.5** | 18.4 | 14.0 | 18.1 | 17.0 | 75.4 |
| find miss | 13.8 | 10.5 | **9.1** | 13.5 | 9.8 | 88.7 |
| find 50% | 19.8 | 24.6 | **19.4** | 20.9 | 21.6 | 106 |
| find hit (mlf 0.9) | **13.2** | 24.6 | 13.9 | 17.7 | 17.2 | 70.1 |
| find miss (mlf 0.9) | 13.9 | 11.3 | **8.8** | 13.1 | 10.0 | 85.8 |
| iterate | 5.4 | 0.8 | 2.9 | **0.8** | 3.9 | 10.7 |

| n=1,200,000 ns/op | absl::flat_hash_map | ankerl::unordered_dense_map | boost::unordered_flat_map | emhash::hash_map8 | sflat::flat_hash_map | std::unordered_map |
|---|---|---|---|---|---|---|
| insert (reserve) | 72.1 | 101 | 66.3 | 61.7 | **30.2** | 206 |
| insert (no reserve) | 86.9 | 107 | 69.9 | 125 | **50.4** | 337 |
| erase+insert | **121** | 195 | 130 | 161 | 137 | 372 |
| find hit | **29.8** | 46.9 | 32.6 | 35.7 | 30.1 | 117 |
| find miss | 24.1 | 25.4 | **13.8** | 25.4 | 17.5 | 147 |
| find 50% | 32.8 | 44.9 | 33.3 | 37.3 | **31.2** | 187 |
| find hit (mlf 0.9) | 33.6 | 47.0 | 36.4 | 37.4 | **28.8** | 118 |
| find miss (mlf 0.9) | 24.3 | 26.9 | **16.3** | 25.3 | 16.3 | 148 |
| iterate | 8.8 | **0.8** | 3.8 | 0.8 | 3.9 | 33.0 |

| n=10,000,000 ns/op | absl::flat_hash_map | ankerl::unordered_dense_map | boost::unordered_flat_map | emhash::hash_map8 | sflat::flat_hash_map | std::unordered_map |
|---|---|---|---|---|---|---|
| insert (reserve) | 145 | 142 | 137 | 79.8 | **44.9** | 241 |
| insert (no reserve) | 141 | 182 | 137 | 174 | **62.5** | 410 |
| erase+insert | 167 | 0.0 | 188 | 194 | **163** | 426 |
| find hit | 43.4 | 52.4 | 42.8 | 46.4 | **41.4** | 130 |
| find miss | 45.8 | 32.2 | **26.0** | 32.3 | 29.9 | 162 |
| find 50% | 49.4 | 49.7 | 44.4 | **43.8** | 44.9 | 205 |
| find hit (mlf 0.9) | 48.9 | 52.8 | 43.1 | 46.8 | **41.2** | 129 |
| find miss (mlf 0.9) | 41.5 | 32.2 | **25.6** | 31.7 | 30.1 | 161 |
| iterate | 8.3 | 0.8 | 3.7 | **0.8** | 4.0 | 38.5 |

### mask_high_bits_uint64_t__uint64_t

| n=1,024 ns/op | absl::flat_hash_map | ankerl::unordered_dense_map | boost::unordered_flat_map | emhash::hash_map8 | sflat::flat_hash_map | std::unordered_map |
|---|---|---|---|---|---|---|
| insert (reserve) | 34.8 | 13.9 | 8.7 | **4.5** | 8.9 | 59.5 |
| insert (no reserve) | 57.4 | 25.0 | 27.3 | **17.9** | 31.7 | 76.2 |
| erase+insert | 56.6 | 18.8 | **10.3** | 22.5 | 43.6 | 57.8 |
| find hit | 6.3 | 6.3 | 6.5 | **3.3** | 6.5 | 13.1 |
| find miss | 141 | 5.8 | **4.9** | 7.8 | 7.0 | 24.9 |
| find 50% | 81.3 | 5.9 | 5.6 | **3.2** | 6.5 | 20.3 |
| find hit (mlf 0.9) | 6.3 | 6.3 | 6.5 | **3.4** | 6.5 | 13.1 |
| find miss (mlf 0.9) | 142 | 5.8 | **4.9** | 7.9 | 7.3 | 25.0 |
| iterate | 3.2 | 0.8 | 3.3 | **0.8** | 4.0 | 1.9 |

| n=100,000 ns/op | absl::flat_hash_map | ankerl::unordered_dense_map | boost::unordered_flat_map | emhash::hash_map8 | sflat::flat_hash_map | std::unordered_map |
|---|---|---|---|---|---|---|
| insert (reserve) | 49.5 | 17.7 | 14.2 | **12.4** | 14.6 | 93.3 |
| insert (no reserve) | 76.9 | 29.2 | **26.7** | 33.7 | 33.8 | 142 |
| erase+insert | 136 | 77.9 | **64.4** | 81.1 | 81.5 | 212 |
| find hit | 13.3 | 19.3 | 14.0 | 17.5 | **13.0** | 50.3 |
| find miss | 56.7 | 9.6 | **6.8** | 8.7 | 8.6 | 71.2 |
| find 50% | 41.7 | 22.4 | 17.9 | **15.7** | 19.0 | 70.4 |
| find hit (mlf 0.9) | 15.7 | 19.7 | 12.7 | 14.5 | **12.5** | 50.4 |
| find miss (mlf 0.9) | 57.4 | 9.8 | **6.8** | 8.8 | 8.7 | 79.5 |
| iterate | 5.6 | **0.8** | 2.8 | 0.8 | 3.9 | 5.2 |

| n=1,200,000 ns/op | absl::flat_hash_map | ankerl::unordered_dense_map | boost::unordered_flat_map | emhash::hash_map8 | sflat::flat_hash_map | std::unordered_map |
|---|---|---|---|---|---|---|
| insert (reserve) | 129 | 98.3 | 59.3 | **24.4** | 28.0 | 161 |
| insert (no reserve) | 157 | 106 | 72.0 | 101 | **47.9** | 281 |
| erase+insert | 180 | 195 | 136 | 167 | **130** | 363 |
| find hit | 28.0 | 44.3 | 32.5 | 33.7 | **26.0** | 95.8 |
| find miss | 111 | 25.2 | **13.4** | 23.3 | 18.1 | 139 |
| find 50% | 87.9 | 42.3 | 33.1 | 31.3 | **30.0** | 137 |
| find hit (mlf 0.9) | 28.0 | 44.0 | 35.9 | 33.3 | **26.7** | 94.1 |
| find miss (mlf 0.9) | 123 | 25.0 | 16.2 | 22.8 | **14.8** | 138 |
| iterate | 9.7 | **0.8** | 3.7 | 0.8 | 3.9 | 22.5 |

| n=10,000,000 ns/op | absl::flat_hash_map | ankerl::unordered_dense_map | boost::unordered_flat_map | emhash::hash_map8 | sflat::flat_hash_map | std::unordered_map |
|---|---|---|---|---|---|---|
| insert (reserve) | 158 | 141 | 131 | **34.9** | 40.9 | 186 |
| insert (no reserve) | 205 | 180 | 136 | 140 | **60.5** | 335 |
| erase+insert | 234 | 0.0 | 186 | 202 | **158** | 403 |
| find hit | 40.9 | 51.1 | 42.2 | 47.0 | **37.4** | 104 |
| find miss | 135 | 32.1 | **25.7** | 29.3 | 27.9 | 149 |
| find 50% | 101 | 60.5 | 43.3 | **39.5** | 42.7 | 151 |
| find hit (mlf 0.9) | 45.1 | 59.8 | 42.3 | 43.1 | **39.1** | 105 |
| find miss (mlf 0.9) | 133 | 33.7 | **25.7** | 28.2 | 28.5 | 149 |
| iterate | 9.2 | 0.8 | 3.5 | **0.8** | 3.9 | 26.3 |

### mask_low_bits_uint64_t__uint64_t

| n=1,024 ns/op | absl::flat_hash_map | ankerl::unordered_dense_map | boost::unordered_flat_map | emhash::hash_map8 | sflat::flat_hash_map | std::unordered_map |
|---|---|---|---|---|---|---|
| insert (reserve) | 174 | 13.8 | **8.7** | 1694 | 11.1 | 58.0 |
| insert (no reserve) | 256 | **24.4** | 27.9 | 2732 | 33.2 | 76.5 |
| erase+insert | 248 | 18.0 | **10.3** | 0.0 | 43.5 | 62.3 |
| find hit | 139 | **6.3** | 6.4 | 0.0 | 6.9 | 12.9 |
| find miss | 249 | 5.8 | **4.9** | 0.0 | 7.2 | 25.0 |
| find 50% | 196 | 5.9 | **5.5** | 0.0 | 6.6 | 20.3 |
| find hit (mlf 0.9) | 140 | **6.2** | 6.5 | 0.0 | 7.0 | 12.9 |
| find miss (mlf 0.9) | 251 | 5.7 | **4.9** | 0.0 | 7.2 | 25.0 |
| iterate | 3.6 | **0.8** | 3.1 | 0.8 | 4.0 | 1.9 |

| n=100,000 ns/op | absl::flat_hash_map | ankerl::unordered_dense_map | boost::unordered_flat_map | emhash::hash_map8 | sflat::flat_hash_map | std::unordered_map |
|---|---|---|---|---|---|---|
| insert (reserve) | 0.0 | 20.2 | **15.2** | 0.0 | 15.8 | 88.8 |
| insert (no reserve) | 0.0 | 31.6 | **28.4** | 0.0 | 30.9 | 143 |
| erase+insert | 0.0 | 79.6 | **67.4** | 0.0 | 80.8 | 219 |
| find hit | 0.0 | 21.5 | 15.9 | 0.0 | **14.2** | 56.8 |
| find miss | 0.0 | 10.9 | **9.2** | 0.0 | 9.4 | 81.0 |
| find 50% | 0.0 | 22.7 | 20.8 | 0.0 | **20.5** | 79.0 |
| find hit (mlf 0.9) | 0.0 | 20.5 | **15.6** | 0.0 | 16.9 | 56.4 |
| find miss (mlf 0.9) | 0.0 | 11.6 | **9.3** | 0.0 | 9.4 | 80.6 |
| iterate | 0.0 | **0.8** | 2.7 | 0.0 | 3.9 | 5.1 |

| n=1,200,000 ns/op | absl::flat_hash_map | ankerl::unordered_dense_map | boost::unordered_flat_map | emhash::hash_map8 | sflat::flat_hash_map | std::unordered_map |
|---|---|---|---|---|---|---|
| insert (reserve) | 0.0 | 100 | 57.8 | 0.0 | **29.2** | 166 |
| insert (no reserve) | 0.0 | 108 | 69.9 | 0.0 | **52.0** | 284 |
| erase+insert | 0.0 | 197 | **134** | 0.0 | 136 | 361 |
| find hit | 0.0 | 48.5 | 32.8 | 0.0 | **28.9** | 96.9 |
| find miss | 0.0 | 27.0 | 15.9 | 0.0 | **15.6** | 142 |
| find 50% | 0.0 | 43.2 | **31.2** | 0.0 | 31.9 | 139 |
| find hit (mlf 0.9) | 0.0 | 44.9 | 32.5 | 0.0 | **29.0** | 95.6 |
| find miss (mlf 0.9) | 0.0 | 25.2 | **13.8** | 0.0 | 16.4 | 142 |
| iterate | 0.0 | **0.8** | 3.8 | 0.0 | 3.9 | 22.6 |

| n=10,000,000 ns/op | absl::flat_hash_map | ankerl::unordered_dense_map | boost::unordered_flat_map | emhash::hash_map8 | sflat::flat_hash_map | std::unordered_map |
|---|---|---|---|---|---|---|
| insert (reserve) | 0.0 | 142 | 130 | 0.0 | **44.2** | 191 |
| insert (no reserve) | 0.0 | 183 | 137 | 0.0 | **62.2** | 341 |
| erase+insert | 0.0 | 0.0 | 186 | 0.0 | **168** | 408 |
| find hit | 0.0 | 53.4 | 43.0 | 0.0 | **40.6** | 105 |
| find miss | 0.0 | 33.9 | **26.5** | 0.0 | 29.6 | 152 |
| find 50% | 0.0 | 50.2 | **43.8** | 0.0 | 44.7 | 148 |
| find hit (mlf 0.9) | 0.0 | 52.1 | 42.7 | 0.0 | **41.6** | 106 |
| find miss (mlf 0.9) | 0.0 | 33.1 | **25.8** | 0.0 | 30.4 | 152 |
| iterate | 0.0 | **0.8** | 3.7 | 0.0 | 3.9 | 26.2 |

### mask_split_bits_uint64_t__56bytes_payload

| n=1,024 ns/op | absl::flat_hash_map | ankerl::unordered_dense_map | boost::unordered_flat_map | emhash::hash_map8 | sflat::flat_hash_map | std::unordered_map |
|---|---|---|---|---|---|---|
| insert (reserve) | 332 | 21.4 | **10.6** | 499 | 12.0 | 69.1 |
| insert (no reserve) | 455 | **34.4** | 51.6 | 791 | 54.4 | 103 |
| erase+insert | 507 | 23.5 | **14.6** | 2071 | 48.4 | 73.2 |
| find hit | 414 | 7.6 | **7.4** | 442 | 7.9 | 20.1 |
| find miss | 204 | 6.5 | **5.4** | 677 | 7.5 | 26.5 |
| find 50% | 328 | 6.7 | **6.4** | 553 | 7.6 | 22.1 |
| find hit (mlf 0.9) | 420 | 7.6 | **7.3** | 443 | 7.8 | 20.1 |
| find miss (mlf 0.9) | 203 | 6.5 | **5.5** | 677 | 7.5 | 26.2 |
| iterate | 3.3 | **0.8** | 2.8 | 0.8 | 4.0 | 4.5 |

| n=100,000 ns/op | absl::flat_hash_map | ankerl::unordered_dense_map | boost::unordered_flat_map | emhash::hash_map8 | sflat::flat_hash_map | std::unordered_map |
|---|---|---|---|---|---|---|
| insert (reserve) | 0.0 | 37.1 | 36.7 | 0.0 | **32.3** | 158 |
| insert (no reserve) | 0.0 | 70.8 | **62.5** | 0.0 | 76.6 | 256 |
| erase+insert | 0.0 | **111** | 128 | 0.0 | 119 | 325 |
| find hit | 0.0 | 34.5 | 31.1 | 0.0 | **30.1** | 92.8 |
| find miss | 0.0 | 16.2 | **13.9** | 0.0 | 14.8 | 126 |
| find 50% | 0.0 | 31.0 | 29.6 | 0.0 | **29.1** | 146 |
| find hit (mlf 0.9) | 0.0 | 32.4 | 31.3 | 0.0 | **28.8** | 98.3 |
| find miss (mlf 0.9) | 0.0 | 15.5 | 14.0 | 0.0 | **14.0** | 128 |
| iterate | 0.0 | **0.8** | 2.6 | 0.0 | 4.0 | 26.9 |

| n=1,200,000 ns/op | absl::flat_hash_map | ankerl::unordered_dense_map | boost::unordered_flat_map | emhash::hash_map8 | sflat::flat_hash_map | std::unordered_map |
|---|---|---|---|---|---|---|
| insert (reserve) | 0.0 | 124 | 136 | 0.0 | **45.9** | 222 |
| insert (no reserve) | 0.0 | 199 | 196 | 0.0 | **84.1** | 382 |
| erase+insert | 0.0 | 202 | 168 | 0.0 | **157** | 414 |
| find hit | 0.0 | 52.6 | 45.4 | 0.0 | **42.0** | 127 |
| find miss | 0.0 | 31.0 | **23.8** | 0.0 | 27.6 | 168 |
| find 50% | 0.0 | 51.9 | 43.3 | 0.0 | **42.6** | 197 |
| find hit (mlf 0.9) | 0.0 | 54.1 | 45.4 | 0.0 | **41.9** | 125 |
| find miss (mlf 0.9) | 0.0 | 31.5 | **23.7** | 0.0 | 27.5 | 166 |
| iterate | 0.0 | **0.8** | 3.6 | 0.0 | 4.0 | 42.9 |

| n=10,000,000 ns/op | absl::flat_hash_map | ankerl::unordered_dense_map | boost::unordered_flat_map | emhash::hash_map8 | sflat::flat_hash_map | std::unordered_map |
|---|---|---|---|---|---|---|
| insert (reserve) | 0.0 | 147 | 226 | 0.0 | **61.3** | 268 |
| insert (no reserve) | 0.0 | 249 | 265 | 0.0 | **99.1** | 442 |
| erase+insert | 0.0 | 0.0 | 271 | 0.0 | **204** | 523 |
| find hit | 0.0 | 74.8 | 69.0 | 0.0 | **48.2** | 155 |
| find miss | 0.0 | 37.5 | **30.0** | 0.0 | 36.5 | 198 |
| find 50% | 0.0 | 76.1 | 62.6 | 0.0 | **50.9** | 246 |
| find hit (mlf 0.9) | 0.0 | 73.2 | 68.3 | 0.0 | **47.8** | 156 |
| find miss (mlf 0.9) | 0.0 | 37.4 | **30.1** | 0.0 | 36.4 | 198 |
| iterate | 0.0 | **0.8** | 3.5 | 0.0 | 4.0 | 58.7 |

### small_string_max_12__uint64_t

| n=1,024 ns/op | absl::flat_hash_map | ankerl::unordered_dense_map | boost::unordered_flat_map | emhash::hash_map8 | sflat::flat_hash_map | std::unordered_map |
|---|---|---|---|---|---|---|
| insert (reserve) | 38.3 | 39.3 | **28.5** | 48.5 | 37.9 | 110 |
| insert (no reserve) | 95.7 | 87.8 | **79.1** | 137 | 95.0 | 135 |
| erase+insert | 63.9 | 58.2 | **40.5** | 78.9 | 103 | 99.3 |
| find hit | 26.1 | 24.6 | 24.7 | **21.2** | 27.0 | 40.4 |
| find miss | 15.0 | 15.4 | **14.0** | 16.3 | 18.6 | 41.7 |
| find 50% | 21.7 | 21.7 | 21.2 | **18.4** | 23.5 | 43.2 |
| find hit (mlf 0.9) | 26.0 | 24.4 | 24.6 | **21.2** | 26.9 | 40.3 |
| find miss (mlf 0.9) | 14.9 | 15.3 | **13.7** | 16.3 | 18.9 | 41.9 |
| iterate | 3.6 | **0.8** | 3.0 | 0.8 | 3.9 | 4.5 |

| n=100,000 ns/op | absl::flat_hash_map | ankerl::unordered_dense_map | boost::unordered_flat_map | emhash::hash_map8 | sflat::flat_hash_map | std::unordered_map |
|---|---|---|---|---|---|---|
| insert (reserve) | 53.0 | 45.0 | **38.6** | 100 | 52.6 | 176 |
| insert (no reserve) | 87.3 | 87.1 | **72.0** | 174 | 95.6 | 297 |
| erase+insert | 165 | **154** | 156 | 206 | 184 | 355 |
| find hit | **64.8** | 74.9 | 70.0 | 81.6 | 69.1 | 199 |
| find miss | 37.9 | 31.7 | **30.0** | 38.6 | 33.5 | 169 |
| find 50% | **58.9** | 65.0 | 60.8 | 67.9 | 60.5 | 215 |
| find hit (mlf 0.9) | **64.5** | 74.7 | 70.0 | 81.2 | 68.4 | 203 |
| find miss (mlf 0.9) | 38.1 | 31.8 | **30.0** | 38.3 | 33.6 | 174 |
| iterate | 5.4 | **0.8** | 2.6 | 0.8 | 3.9 | 27.0 |

| n=1,200,000 ns/op | absl::flat_hash_map | ankerl::unordered_dense_map | boost::unordered_flat_map | emhash::hash_map8 | sflat::flat_hash_map | std::unordered_map |
|---|---|---|---|---|---|---|
| insert (reserve) | 85.8 | 100 | 92.3 | 142 | **78.3** | 253 |
| insert (no reserve) | 128 | 143 | **109** | 307 | 131 | 427 |
| erase+insert | **178** | 239 | 198 | 266 | 235 | 452 |
| find hit | 90.3 | 123 | 109 | 120 | **90.1** | 271 |
| find miss | 48.9 | 59.0 | 52.2 | 67.6 | **44.1** | 250 |
| find 50% | 81.8 | 108 | 96.0 | 104 | **77.7** | 293 |
| find hit (mlf 0.9) | 90.9 | 122 | 104 | 120 | **90.1** | 272 |
| find miss (mlf 0.9) | 48.5 | 59.0 | 52.5 | 67.8 | **42.2** | 251 |
| iterate | 8.8 | **0.8** | 3.9 | 0.8 | 3.9 | 42.5 |

| n=10,000,000 ns/op | absl::flat_hash_map | ankerl::unordered_dense_map | boost::unordered_flat_map | emhash::hash_map8 | sflat::flat_hash_map | std::unordered_map |
|---|---|---|---|---|---|---|
| insert (reserve) | 130 | 115 | 127 | 161 | **101** | 284 |
| insert (no reserve) | 164 | 170 | 151 | 351 | **148** | 502 |
| erase+insert | **254** | 0.0 | 268 | 317 | 286 | 544 |
| find hit | 115 | 144 | 112 | 134 | **112** | 318 |
| find miss | 76.2 | 67.7 | **59.5** | 75.2 | 61.3 | 290 |
| find 50% | 107 | 122 | 108 | 126 | **101** | 340 |
| find hit (mlf 0.9) | 114 | 139 | 112 | 142 | **112** | 311 |
| find miss (mlf 0.9) | 76.0 | 67.2 | **59.6** | 75.7 | 61.1 | 287 |
| iterate | 8.4 | 0.8 | 3.6 | **0.8** | 3.9 | 54.5 |

### small_string_fix_12__uint64_t

| n=1,024 ns/op | absl::flat_hash_map | ankerl::unordered_dense_map | boost::unordered_flat_map | emhash::hash_map8 | sflat::flat_hash_map | std::unordered_map |
|---|---|---|---|---|---|---|
| insert (reserve) | 29.3 | 31.6 | **23.7** | 36.6 | 30.7 | 93.9 |
| insert (no reserve) | 70.3 | 64.4 | **61.8** | 100 | 80.5 | 116 |
| erase+insert | 53.2 | 50.9 | **33.8** | 59.6 | 118 | 89.9 |
| find hit | 23.7 | **23.7** | 23.9 | 24.0 | 25.9 | 45.9 |
| find miss | 16.8 | 15.9 | **14.9** | 17.5 | 20.2 | 48.3 |
| find 50% | 25.5 | 25.0 | 23.8 | **22.1** | 27.4 | 49.2 |
| find hit (mlf 0.9) | **23.7** | 23.8 | 23.9 | 23.8 | 25.7 | 45.8 |
| find miss (mlf 0.9) | 16.5 | 16.0 | **14.9** | 17.5 | 20.2 | 48.4 |
| iterate | 3.3 | **0.8** | 3.1 | 0.8 | 3.9 | 4.5 |

| n=100,000 ns/op | absl::flat_hash_map | ankerl::unordered_dense_map | boost::unordered_flat_map | emhash::hash_map8 | sflat::flat_hash_map | std::unordered_map |
|---|---|---|---|---|---|---|
| insert (reserve) | 49.6 | 38.6 | **35.5** | 93.8 | 48.0 | 169 |
| insert (no reserve) | 73.6 | 72.5 | **61.6** | 147 | 89.2 | 278 |
| erase+insert | 155 | 154 | **153** | 198 | 170 | 346 |
| find hit | **64.1** | 72.7 | 68.8 | 79.1 | 66.8 | 226 |
| find miss | 33.5 | 27.6 | **24.1** | 32.2 | 25.2 | 183 |
| find 50% | **56.4** | 62.4 | 58.7 | 65.7 | 56.6 | 217 |
| find hit (mlf 0.9) | **64.2** | 73.1 | 68.4 | 78.9 | 65.7 | 223 |
| find miss (mlf 0.9) | 33.5 | 27.6 | **24.1** | 32.0 | 25.6 | 183 |
| iterate | 5.4 | 0.8 | 2.9 | **0.8** | 3.9 | 26.5 |

| n=1,200,000 ns/op | absl::flat_hash_map | ankerl::unordered_dense_map | boost::unordered_flat_map | emhash::hash_map8 | sflat::flat_hash_map | std::unordered_map |
|---|---|---|---|---|---|---|
| insert (reserve) | 82.8 | 99.2 | **71.5** | 142 | 76.9 | 239 |
| insert (no reserve) | 113 | 136 | **94.8** | 298 | 128 | 407 |
| erase+insert | **179** | 242 | 193 | 255 | 217 | 446 |
| find hit | 91.4 | 122 | 95.9 | 120 | **89.8** | 315 |
| find miss | 47.2 | 59.9 | 43.0 | 63.2 | **39.5** | 267 |
| find 50% | 79.1 | 103 | 84.8 | 101 | **75.4** | 303 |
| find hit (mlf 0.9) | 93.4 | 121 | 94.8 | 120 | **89.2** | 313 |
| find miss (mlf 0.9) | 47.7 | 59.7 | 44.3 | 63.2 | **37.8** | 267 |
| iterate | 8.8 | 0.8 | 3.9 | **0.8** | 3.9 | 42.3 |

| n=10,000,000 ns/op | absl::flat_hash_map | ankerl::unordered_dense_map | boost::unordered_flat_map | emhash::hash_map8 | sflat::flat_hash_map | std::unordered_map |
|---|---|---|---|---|---|---|
| insert (reserve) | 128 | 115 | 116 | 164 | **106** | 271 |
| insert (no reserve) | 151 | 169 | **136** | 343 | 160 | 482 |
| erase+insert | **254** | 0.0 | 271 | 313 | 276 | 541 |
| find hit | 117 | 140 | 113 | 136 | **112** | 357 |
| find miss | 75.0 | 68.8 | 60.3 | 70.1 | **60.1** | 312 |
| find 50% | 106 | 119 | 107 | 116 | **100** | 356 |
| find hit (mlf 0.9) | 117 | 136 | 113 | 136 | **112** | 355 |
| find miss (mlf 0.9) | 75.7 | 68.3 | **59.4** | 70.1 | 60.1 | 307 |
| iterate | 8.3 | **0.8** | 3.6 | 0.8 | 3.9 | 54.1 |

### mid_string_max_24__uint64_t

| n=1,024 ns/op | absl::flat_hash_map | ankerl::unordered_dense_map | boost::unordered_flat_map | emhash::hash_map8 | sflat::flat_hash_map | std::unordered_map |
|---|---|---|---|---|---|---|
| insert (reserve) | 58.4 | 52.7 | **47.9** | 62.2 | 55.6 | 120 |
| insert (no reserve) | 116 | **96.3** | 104 | 159 | 133 | 147 |
| erase+insert | 99.4 | 91.5 | **72.5** | 111 | 146 | 133 |
| find hit | 33.7 | 33.3 | 33.1 | **30.4** | 33.8 | 50.4 |
| find miss | 17.7 | 17.8 | **16.7** | 18.0 | 21.7 | 47.4 |
| find 50% | 27.1 | 27.1 | 26.9 | **24.5** | 29.7 | 50.8 |
| find hit (mlf 0.9) | 33.7 | 33.4 | 33.5 | **30.5** | 34.6 | 50.0 |
| find miss (mlf 0.9) | 17.7 | 17.7 | **17.0** | 17.8 | 21.7 | 47.0 |
| iterate | 3.4 | **0.8** | 3.1 | 0.8 | 3.9 | 4.5 |

| n=100,000 ns/op | absl::flat_hash_map | ankerl::unordered_dense_map | boost::unordered_flat_map | emhash::hash_map8 | sflat::flat_hash_map | std::unordered_map |
|---|---|---|---|---|---|---|
| insert (reserve) | 84.9 | 68.8 | **65.0** | 140 | 77.4 | 215 |
| insert (no reserve) | 121 | 115 | **103** | 219 | 138 | 333 |
| erase+insert | 257 | **243** | 251 | 302 | 286 | 422 |
| find hit | **116** | 126 | 119 | 131 | 120 | 249 |
| find miss | 60.1 | 58.2 | **51.3** | 58.6 | 59.4 | 211 |
| find 50% | 102 | **100** | 102 | 109 | 101 | 236 |
| find hit (mlf 0.9) | 122 | 123 | 124 | 140 | **120** | 248 |
| find miss (mlf 0.9) | 63.6 | 55.7 | **53.5** | 60.1 | 59.3 | 210 |
| iterate | 5.4 | **0.8** | 2.9 | 0.8 | 3.9 | 27.0 |

| n=1,200,000 ns/op | absl::flat_hash_map | ankerl::unordered_dense_map | boost::unordered_flat_map | emhash::hash_map8 | sflat::flat_hash_map | std::unordered_map |
|---|---|---|---|---|---|---|
| insert (reserve) | 128 | 124 | **108** | 180 | 112 | 283 |
| insert (no reserve) | 201 | 180 | **176** | 373 | 225 | 450 |
| erase+insert | 238 | 293 | **232** | 355 | 334 | 492 |
| find hit | 145 | 173 | 152 | 174 | **142** | 298 |
| find miss | 77.8 | 80.3 | **68.2** | 85.9 | 68.9 | 283 |
| find 50% | 124 | 140 | 126 | 137 | **119** | 334 |
| find hit (mlf 0.9) | 146 | 173 | 152 | 168 | **142** | 302 |
| find miss (mlf 0.9) | 77.1 | 80.8 | **67.2** | 84.4 | 70.2 | 287 |
| iterate | 8.8 | 0.8 | 3.9 | **0.8** | 3.9 | 48.9 |

| n=10,000,000 ns/op | absl::flat_hash_map | ankerl::unordered_dense_map | boost::unordered_flat_map | emhash::hash_map8 | sflat::flat_hash_map | std::unordered_map |
|---|---|---|---|---|---|---|
| insert (reserve) | 163 | 141 | 153 | 208 | **133** | 321 |
| insert (no reserve) | 247 | **209** | 231 | 428 | 255 | 522 |
| erase+insert | **325** | 0.0 | 333 | 437 | 425 | 620 |
| find hit | **190** | 227 | 193 | 214 | 191 | 368 |
| find miss | 111 | 97.9 | **86.4** | 104 | 98.5 | 349 |
| find 50% | 164 | 185 | 160 | 175 | **156** | 394 |
| find hit (mlf 0.9) | 186 | 227 | 184 | 215 | **168** | 365 |
| find miss (mlf 0.9) | 107 | 91.5 | **87.6** | 93.0 | 91.4 | 338 |
| iterate | 8.3 | 0.8 | 3.6 | **0.8** | 3.9 | 61.4 |

### mid_string_fix_24__uint64_t

| n=1,024 ns/op | absl::flat_hash_map | ankerl::unordered_dense_map | boost::unordered_flat_map | emhash::hash_map8 | sflat::flat_hash_map | std::unordered_map |
|---|---|---|---|---|---|---|
| insert (reserve) | 58.5 | 54.8 | **52.2** | 62.6 | 58.3 | 118 |
| insert (no reserve) | 99.4 | **83.1** | 92.1 | 135 | 136 | 140 |
| erase+insert | 130 | 130 | **112** | 151 | 176 | 192 |
| find hit | 54.5 | 54.7 | 52.8 | **51.2** | 55.5 | 88.9 |
| find miss | 26.7 | 25.7 | **23.7** | 24.2 | 30.0 | 75.8 |
| find 50% | 46.2 | 44.9 | 42.3 | **38.1** | 46.9 | 89.1 |
| find hit (mlf 0.9) | 55.0 | 53.8 | 53.4 | **51.8** | 55.8 | 88.1 |
| find miss (mlf 0.9) | 26.5 | 26.1 | **24.1** | 24.2 | 30.5 | 75.1 |
| iterate | 3.4 | **0.8** | 3.2 | 0.8 | 3.9 | 12.2 |

| n=100,000 ns/op | absl::flat_hash_map | ankerl::unordered_dense_map | boost::unordered_flat_map | emhash::hash_map8 | sflat::flat_hash_map | std::unordered_map |
|---|---|---|---|---|---|---|
| insert (reserve) | 119 | 91.9 | **83.9** | 178 | 86.3 | 239 |
| insert (no reserve) | 161 | **116** | 143 | 239 | 199 | 371 |
| erase+insert | 337 | **299** | 398 | 367 | 372 | 465 |
| find hit | **168** | 182 | 170 | 180 | 170 | 278 |
| find miss | 82.6 | 82.7 | 71.7 | **65.5** | 89.4 | 233 |
| find 50% | 145 | 144 | 139 | **124** | 142 | 292 |
| find hit (mlf 0.9) | **169** | 182 | 170 | 176 | 169 | 280 |
| find miss (mlf 0.9) | 82.9 | 82.6 | 71.6 | **65.0** | 89.9 | 234 |
| iterate | 5.4 | **0.8** | 2.8 | 0.8 | 3.9 | 30.9 |

| n=1,200,000 ns/op | absl::flat_hash_map | ankerl::unordered_dense_map | boost::unordered_flat_map | emhash::hash_map8 | sflat::flat_hash_map | std::unordered_map |
|---|---|---|---|---|---|---|
| insert (reserve) | 174 | 147 | 144 | 209 | **135** | 302 |
| insert (no reserve) | 324 | **190** | 290 | 402 | 345 | 471 |
| erase+insert | 293 | 355 | **287** | 401 | 406 | 540 |
| find hit | 207 | 221 | **201** | 222 | 203 | 299 |
| find miss | 109 | 114 | **83.9** | 88.0 | 111 | 311 |
| find 50% | 165 | 174 | 165 | **164** | 165 | 362 |
| find hit (mlf 0.9) | **189** | 222 | 198 | 219 | 196 | 302 |
| find miss (mlf 0.9) | 106 | 107 | **82.7** | 85.0 | 105 | 308 |
| iterate | 8.8 | 0.8 | 3.8 | **0.8** | 3.9 | 52.2 |

| n=10,000,000 ns/op | absl::flat_hash_map | ankerl::unordered_dense_map | boost::unordered_flat_map | emhash::hash_map8 | sflat::flat_hash_map | std::unordered_map |
|---|---|---|---|---|---|---|
| insert (reserve) | 214 | 162 | 218 | 253 | **159** | 343 |
| insert (no reserve) | 396 | **220** | 385 | 475 | 399 | 567 |
| erase+insert | **412** | 0.0 | 417 | 538 | 555 | 681 |
| find hit | 280 | 324 | 290 | 331 | **280** | 411 |
| find miss | 166 | 147 | 126 | **109** | 154 | 415 |
| find 50% | 234 | 248 | 227 | 231 | **210** | 467 |
| find hit (mlf 0.9) | 271 | 321 | 279 | 311 | **250** | 411 |
| find miss (mlf 0.9) | 151 | 129 | 102 | **98.3** | 135 | 393 |
| iterate | 8.3 | 0.8 | 3.6 | **0.8** | 3.9 | 66.8 |

### long_string_max_64__uint64_t

| n=1,024 ns/op | absl::flat_hash_map | ankerl::unordered_dense_map | boost::unordered_flat_map | emhash::hash_map8 | sflat::flat_hash_map | std::unordered_map |
|---|---|---|---|---|---|---|
| insert (reserve) | 80.6 | 68.0 | **66.2** | 81.3 | 77.8 | 138 |
| insert (no reserve) | 143 | **116** | 129 | 185 | 174 | 168 |
| erase+insert | 132 | 132 | **107** | 149 | 189 | 197 |
| find hit | 55.4 | 55.4 | 55.8 | **52.9** | 55.9 | 102 |
| find miss | 28.8 | 28.2 | 27.2 | **27.1** | 31.8 | 81.5 |
| find 50% | 45.6 | 44.9 | 43.6 | **42.0** | 48.1 | 93.9 |
| find hit (mlf 0.9) | 55.2 | 55.6 | 55.7 | **53.1** | 56.5 | 100 |
| find miss (mlf 0.9) | 28.6 | 27.9 | **26.7** | 26.8 | 32.0 | 81.5 |
| iterate | 3.3 | **0.8** | 3.2 | 0.8 | 3.9 | 13.0 |

| n=100,000 ns/op | absl::flat_hash_map | ankerl::unordered_dense_map | boost::unordered_flat_map | emhash::hash_map8 | sflat::flat_hash_map | std::unordered_map |
|---|---|---|---|---|---|---|
| insert (reserve) | 109 | 92.1 | **82.5** | 182 | 92.9 | 244 |
| insert (no reserve) | 167 | **134** | 145 | 270 | 190 | 383 |
| erase+insert | 340 | **312** | 352 | 395 | 399 | 488 |
| find hit | **163** | 188 | 176 | 186 | 166 | 353 |
| find miss | 88.5 | 91.6 | **83.8** | 85.5 | 90.2 | 289 |
| find 50% | **137** | 149 | 143 | 145 | 142 | 342 |
| find hit (mlf 0.9) | **163** | 191 | 177 | 187 | 165 | 348 |
| find miss (mlf 0.9) | 88.6 | 86.8 | **84.4** | 86.4 | 90.6 | 279 |
| iterate | 5.4 | **0.8** | 2.6 | 0.8 | 3.9 | 66.5 |

| n=1,200,000 ns/op | absl::flat_hash_map | ankerl::unordered_dense_map | boost::unordered_flat_map | emhash::hash_map8 | sflat::flat_hash_map | std::unordered_map |
|---|---|---|---|---|---|---|
| insert (reserve) | 194 | 148 | **131** | 244 | 136 | 307 |
| insert (no reserve) | 335 | **221** | 286 | 461 | 315 | 484 |
| erase+insert | 298 | 376 | **292** | 410 | 441 | 549 |
| find hit | 210 | 248 | 214 | 244 | **200** | 344 |
| find miss | 110 | 118 | **99.2** | 117 | 103 | 323 |
| find 50% | 189 | 191 | 175 | 187 | **166** | 370 |
| find hit (mlf 0.9) | 213 | 239 | 212 | 237 | **199** | 344 |
| find miss (mlf 0.9) | 110 | 107 | **96.6** | 111 | 103 | 324 |
| iterate | 8.8 | 0.8 | 3.9 | **0.8** | 3.9 | 59.1 |

| n=10,000,000 ns/op | absl::flat_hash_map | ankerl::unordered_dense_map | boost::unordered_flat_map | emhash::hash_map8 | sflat::flat_hash_map | std::unordered_map |
|---|---|---|---|---|---|---|
| insert (reserve) | 229 | 206 | 206 | 287 | **167** | 364 |
| insert (no reserve) | 407 | **312** | 374 | 535 | 364 | 572 |
| erase+insert | 402 | 0.0 | **400** | 555 | 573 | 736 |
| find hit | 292 | 336 | 290 | 343 | **267** | 450 |
| find miss | 164 | 145 | **136** | 141 | 146 | 415 |
| find 50% | 237 | 261 | 238 | 261 | **217** | 472 |
| find hit (mlf 0.9) | 285 | 333 | 285 | 348 | **266** | 447 |
| find miss (mlf 0.9) | 152 | 130 | **118** | 128 | 131 | 408 |
| iterate | 8.3 | 0.8 | 3.7 | **0.8** | 3.9 | 73.9 |

### long_string_fix_64__uint64_t

| n=1,024 ns/op | absl::flat_hash_map | ankerl::unordered_dense_map | boost::unordered_flat_map | emhash::hash_map8 | sflat::flat_hash_map | std::unordered_map |
|---|---|---|---|---|---|---|
| insert (reserve) | 70.4 | 66.6 | **65.5** | 76.6 | 70.3 | 132 |
| insert (no reserve) | 133 | **108** | 121 | 168 | 169 | 163 |
| erase+insert | 154 | 151 | **131** | 165 | 212 | 186 |
| find hit | 75.0 | **70.9** | 73.2 | 74.0 | 75.5 | 129 |
| find miss | 42.4 | 39.4 | **39.0** | 41.0 | 45.4 | 101 |
| find 50% | 65.2 | 65.1 | 64.6 | **60.2** | 67.7 | 120 |
| find hit (mlf 0.9) | 74.6 | **70.8** | 72.6 | 73.7 | 79.8 | 130 |
| find miss (mlf 0.9) | 42.7 | 39.1 | **38.5** | 41.2 | 45.5 | 102 |
| iterate | 3.4 | **0.8** | 3.1 | 0.8 | 3.9 | 13.7 |

| n=100,000 ns/op | absl::flat_hash_map | ankerl::unordered_dense_map | boost::unordered_flat_map | emhash::hash_map8 | sflat::flat_hash_map | std::unordered_map |
|---|---|---|---|---|---|---|
| insert (reserve) | 135 | 114 | **106** | 225 | 110 | 267 |
| insert (no reserve) | 223 | **144** | 196 | 330 | 247 | 422 |
| erase+insert | 383 | **314** | 413 | 406 | 457 | 487 |
| find hit | **194** | 234 | 202 | 240 | 203 | 396 |
| find miss | 121 | 114 | 114 | **108** | 120 | 308 |
| find 50% | **169** | 184 | 174 | 180 | 173 | 371 |
| find hit (mlf 0.9) | **194** | 233 | 203 | 238 | 204 | 401 |
| find miss (mlf 0.9) | 121 | 115 | 113 | **110** | 119 | 311 |
| iterate | 5.4 | 0.8 | 2.7 | **0.8** | 3.9 | 69.6 |

| n=1,200,000 ns/op | absl::flat_hash_map | ankerl::unordered_dense_map | boost::unordered_flat_map | emhash::hash_map8 | sflat::flat_hash_map | std::unordered_map |
|---|---|---|---|---|---|---|
| insert (reserve) | 190 | 165 | 168 | 240 | **159** | 330 |
| insert (no reserve) | 362 | **220** | 330 | 491 | 399 | 513 |
| erase+insert | 327 | 368 | **314** | 443 | 536 | 580 |
| find hit | **244** | 308 | 259 | 300 | 285 | 385 |
| find miss | 147 | 138 | **128** | 135 | 153 | 354 |
| find 50% | 234 | 229 | **211** | 226 | 231 | 402 |
| find hit (mlf 0.9) | 273 | 308 | **259** | 302 | 280 | 383 |
| find miss (mlf 0.9) | 156 | 140 | **124** | 134 | 141 | 351 |
| iterate | 8.9 | **0.8** | 3.8 | 0.8 | 3.9 | 57.6 |

| n=10,000,000 ns/op | absl::flat_hash_map | ankerl::unordered_dense_map | boost::unordered_flat_map | emhash::hash_map8 | sflat::flat_hash_map | std::unordered_map |
|---|---|---|---|---|---|---|
| insert (reserve) | 232 | 191 | 242 | 287 | **178** | 372 |
| insert (no reserve) | 438 | **265** | 470 | 581 | 459 | 616 |
| erase+insert | 437 | 0.0 | **432** | 581 | 684 | 794 |
| find hit | **346** | 431 | 365 | 429 | 352 | 504 |
| find miss | 206 | 188 | 181 | **179** | 194 | 458 |
| find 50% | 291 | 323 | 305 | 323 | **288** | 523 |
| find hit (mlf 0.9) | **351** | 425 | 360 | 430 | 360 | 507 |
| find miss (mlf 0.9) | 198 | 172 | 170 | **167** | 178 | 455 |
| iterate | 8.3 | **0.8** | 3.6 | 0.8 | 3.9 | 74.2 |

## Heap memory

### mask_split_bits_uint64_t__uint64_t

Heap bytes per element after inserting n keys with reserve(n) (final / peak), and load factor.

| n | absl::flat_hash_map | ankerl::unordered_dense_map | boost::unordered_flat_map | emhash::hash_map8 | sflat::flat_hash_map | std::unordered_map |
|---|---|---|---|---|---|---|
| 1,638 | 21.2 / 21.2 (lf 0.80) | 22.9 / 22.9 (lf 0.80) | 20.0 / 20.0 (lf 0.85) | 52.1 / 52.1 (lf 0.40) | 19.7 / 19.7 (lf 0.88) | 32.5 / 32.5 (lf 0.94) |
| 104,857 | 0.0 / 0.0 (lf 0.00) | 22.9 / 22.9 (lf 0.80) | 20.0 / 20.0 (lf 0.85) | 0.0 / 0.0 (lf 0.00) | 19.7 / 19.7 (lf 0.87) | 32.2 / 32.2 (lf 0.97) |
| 1,258,291 | 0.0 / 0.0 (lf 0.00) | 25.2 / 25.2 (lf 0.60) | 26.7 / 26.7 (lf 0.64) | 0.0 / 0.0 (lf 0.00) | 19.7 / 19.7 (lf 0.87) | 32.5 / 32.5 (lf 0.94) |
| 10,000,000 | 0.0 / 0.0 (lf 0.00) | 25.2 / 25.2 (lf 0.60) | 26.8 / 26.8 (lf 0.64) | 0.0 / 0.0 (lf 0.00) | 19.7 / 19.7 (lf 0.88) | 32.3 / 32.3 (lf 0.97) |

Total MiB at the largest size (final, default max_load_factor / after max_load_factor(0.9)+rehash):

| map | final MiB | peak MiB | final MiB (mlf 0.9) | lf | lf (mlf 0.9) |
|---|---|---|---|---|---|
| absl::flat_hash_map | 0.0 | 0.0 | 0.0 | 0.000 | 0.000 |
| ankerl::unordered_dense_map | 240.6 | 240.6 | 240.6 | 0.596 | 0.596 |
| boost::unordered_flat_map | 256.0 | 256.0 | 256.0 | 0.636 | 0.636 |
| emhash::hash_map8 | 0.0 | 0.0 | 0.0 | 0.000 | 0.000 |
| sflat::flat_hash_map | 188.0 | 188.0 | 188.0 | 0.875 | 0.875 |
| std::unordered_map | 307.9 | 307.9 | 307.9 | 0.966 | 0.966 |

### uniform_uint64_t__uint64_t

Heap bytes per element after inserting n keys with reserve(n) (final / peak), and load factor.

| n | absl::flat_hash_map | ankerl::unordered_dense_map | boost::unordered_flat_map | emhash::hash_map8 | sflat::flat_hash_map | std::unordered_map |
|---|---|---|---|---|---|---|
| 1,638 | 21.2 / 21.2 (lf 0.80) | 22.9 / 22.9 (lf 0.80) | 20.0 / 20.0 (lf 0.85) | 52.1 / 52.1 (lf 0.40) | 19.7 / 19.7 (lf 0.88) | 32.5 / 32.5 (lf 0.94) |
| 104,857 | 21.2 / 21.2 (lf 0.80) | 22.9 / 22.9 (lf 0.80) | 20.0 / 20.0 (lf 0.85) | 52.0 / 52.0 (lf 0.40) | 19.7 / 19.7 (lf 0.87) | 32.2 / 32.2 (lf 0.97) |
| 1,258,291 | 28.3 / 28.3 (lf 0.60) | 25.2 / 25.2 (lf 0.60) | 26.7 / 26.7 (lf 0.64) | 34.7 / 34.7 (lf 0.60) | 19.7 / 19.7 (lf 0.87) | 32.5 / 32.5 (lf 0.94) |
| 10,000,000 | 28.5 / 28.5 (lf 0.60) | 25.2 / 25.2 (lf 0.60) | 26.8 / 26.8 (lf 0.64) | 34.9 / 34.9 (lf 0.60) | 19.7 / 19.7 (lf 0.88) | 32.3 / 32.3 (lf 0.97) |

Total MiB at the largest size (final, default max_load_factor / after max_load_factor(0.9)+rehash):

| map | final MiB | peak MiB | final MiB (mlf 0.9) | lf | lf (mlf 0.9) |
|---|---|---|---|---|---|
| absl::flat_hash_map | 272.0 | 272.0 | 272.0 | 0.596 | 0.596 |
| ankerl::unordered_dense_map | 240.6 | 240.6 | 240.6 | 0.596 | 0.596 |
| boost::unordered_flat_map | 256.0 | 256.0 | 256.0 | 0.636 | 0.636 |
| emhash::hash_map8 | 332.8 | 332.8 | 332.8 | 0.596 | 0.596 |
| sflat::flat_hash_map | 188.0 | 188.0 | 188.0 | 0.875 | 0.875 |
| std::unordered_map | 307.9 | 307.9 | 307.9 | 0.966 | 0.966 |

### mask_high_bits_uint64_t__uint64_t

Heap bytes per element after inserting n keys with reserve(n) (final / peak), and load factor.

| n | absl::flat_hash_map | ankerl::unordered_dense_map | boost::unordered_flat_map | emhash::hash_map8 | sflat::flat_hash_map | std::unordered_map |
|---|---|---|---|---|---|---|
| 1,638 | 21.2 / 21.2 (lf 0.80) | 22.9 / 22.9 (lf 0.80) | 20.0 / 20.0 (lf 0.85) | 52.1 / 52.1 (lf 0.40) | 19.7 / 19.7 (lf 0.88) | 32.5 / 32.5 (lf 0.94) |
| 104,857 | 21.2 / 21.2 (lf 0.80) | 22.9 / 22.9 (lf 0.80) | 20.0 / 20.0 (lf 0.85) | 52.0 / 52.0 (lf 0.40) | 19.7 / 19.7 (lf 0.87) | 32.2 / 32.2 (lf 0.97) |
| 1,258,291 | 28.3 / 28.3 (lf 0.60) | 25.2 / 25.2 (lf 0.60) | 26.7 / 26.7 (lf 0.64) | 34.7 / 34.7 (lf 0.60) | 19.7 / 19.7 (lf 0.87) | 32.5 / 32.5 (lf 0.94) |
| 10,000,000 | 28.5 / 28.5 (lf 0.60) | 25.2 / 25.2 (lf 0.60) | 26.8 / 26.8 (lf 0.64) | 34.9 / 34.9 (lf 0.60) | 19.7 / 19.7 (lf 0.88) | 32.3 / 32.3 (lf 0.97) |

Total MiB at the largest size (final, default max_load_factor / after max_load_factor(0.9)+rehash):

| map | final MiB | peak MiB | final MiB (mlf 0.9) | lf | lf (mlf 0.9) |
|---|---|---|---|---|---|
| absl::flat_hash_map | 272.0 | 272.0 | 272.0 | 0.596 | 0.596 |
| ankerl::unordered_dense_map | 240.6 | 240.6 | 240.6 | 0.596 | 0.596 |
| boost::unordered_flat_map | 256.0 | 256.0 | 256.0 | 0.636 | 0.636 |
| emhash::hash_map8 | 332.8 | 332.8 | 332.8 | 0.596 | 0.596 |
| sflat::flat_hash_map | 188.0 | 188.0 | 188.0 | 0.875 | 0.875 |
| std::unordered_map | 307.9 | 307.9 | 307.9 | 0.966 | 0.966 |

### mask_low_bits_uint64_t__uint64_t

Heap bytes per element after inserting n keys with reserve(n) (final / peak), and load factor.

| n | absl::flat_hash_map | ankerl::unordered_dense_map | boost::unordered_flat_map | emhash::hash_map8 | sflat::flat_hash_map | std::unordered_map |
|---|---|---|---|---|---|---|
| 1,638 | 21.2 / 21.2 (lf 0.80) | 22.9 / 22.9 (lf 0.80) | 20.0 / 20.0 (lf 0.85) | 0.0 / 0.0 (lf 0.00) | 19.7 / 19.7 (lf 0.88) | 32.5 / 32.5 (lf 0.94) |
| 104,857 | 0.0 / 0.0 (lf 0.00) | 22.9 / 22.9 (lf 0.80) | 20.0 / 20.0 (lf 0.85) | 0.0 / 0.0 (lf 0.00) | 19.7 / 19.7 (lf 0.87) | 32.2 / 32.2 (lf 0.97) |
| 1,258,291 | 0.0 / 0.0 (lf 0.00) | 25.2 / 25.2 (lf 0.60) | 26.7 / 26.7 (lf 0.64) | 0.0 / 0.0 (lf 0.00) | 19.7 / 19.7 (lf 0.87) | 32.5 / 32.5 (lf 0.94) |
| 10,000,000 | 0.0 / 0.0 (lf 0.00) | 25.2 / 25.2 (lf 0.60) | 26.8 / 26.8 (lf 0.64) | 0.0 / 0.0 (lf 0.00) | 19.7 / 19.7 (lf 0.88) | 32.3 / 32.3 (lf 0.97) |

Total MiB at the largest size (final, default max_load_factor / after max_load_factor(0.9)+rehash):

| map | final MiB | peak MiB | final MiB (mlf 0.9) | lf | lf (mlf 0.9) |
|---|---|---|---|---|---|
| absl::flat_hash_map | 0.0 | 0.0 | 0.0 | 0.000 | 0.000 |
| ankerl::unordered_dense_map | 240.6 | 240.6 | 240.6 | 0.596 | 0.596 |
| boost::unordered_flat_map | 256.0 | 256.0 | 256.0 | 0.636 | 0.636 |
| emhash::hash_map8 | 0.0 | 0.0 | 0.0 | 0.000 | 0.000 |
| sflat::flat_hash_map | 188.0 | 188.0 | 188.0 | 0.875 | 0.875 |
| std::unordered_map | 307.9 | 307.9 | 307.9 | 0.966 | 0.966 |

### mask_split_bits_uint64_t__56bytes_payload

Heap bytes per element after inserting n keys with reserve(n) (final / peak), and load factor.

| n | absl::flat_hash_map | ankerl::unordered_dense_map | boost::unordered_flat_map | emhash::hash_map8 | sflat::flat_hash_map | std::unordered_map |
|---|---|---|---|---|---|---|
| 1,638 | 81.1 / 81.1 (lf 0.80) | 70.9 / 70.9 (lf 0.80) | 76.3 / 76.3 (lf 0.85) | 148.2 / 148.2 (lf 0.40) | 74.6 / 74.6 (lf 0.88) | 80.5 / 80.5 (lf 0.94) |
| 104,857 | 0.0 / 0.0 (lf 0.00) | 70.9 / 70.9 (lf 0.80) | 76.3 / 76.3 (lf 0.85) | 0.0 / 0.0 (lf 0.00) | 74.6 / 74.6 (lf 0.87) | 80.2 / 80.2 (lf 0.97) |
| 1,258,291 | 0.0 / 0.0 (lf 0.00) | 73.2 / 73.2 (lf 0.60) | 101.7 / 101.7 (lf 0.64) | 0.0 / 0.0 (lf 0.00) | 74.6 / 74.6 (lf 0.87) | 80.5 / 80.5 (lf 0.94) |
| 10,000,000 | 0.0 / 0.0 (lf 0.00) | 73.2 / 73.2 (lf 0.60) | 102.3 / 102.3 (lf 0.64) | 0.0 / 0.0 (lf 0.00) | 74.6 / 74.6 (lf 0.88) | 80.3 / 80.3 (lf 0.97) |

Total MiB at the largest size (final, default max_load_factor / after max_load_factor(0.9)+rehash):

| map | final MiB | peak MiB | final MiB (mlf 0.9) | lf | lf (mlf 0.9) |
|---|---|---|---|---|---|
| absl::flat_hash_map | 0.0 | 0.0 | 0.0 | 0.000 | 0.000 |
| ankerl::unordered_dense_map | 698.4 | 698.4 | 698.4 | 0.596 | 0.596 |
| boost::unordered_flat_map | 976.0 | 976.0 | 976.0 | 0.636 | 0.636 |
| emhash::hash_map8 | 0.0 | 0.0 | 0.0 | 0.000 | 0.000 |
| sflat::flat_hash_map | 711.2 | 711.2 | 711.2 | 0.875 | 0.875 |
| std::unordered_map | 765.6 | 765.6 | 765.6 | 0.966 | 0.966 |

### small_string_max_12__uint64_t

Heap bytes per element after inserting n keys with reserve(n) (final / peak), and load factor.

| n | absl::flat_hash_map | ankerl::unordered_dense_map | boost::unordered_flat_map | emhash::hash_map8 | sflat::flat_hash_map | std::unordered_map |
|---|---|---|---|---|---|---|
| 1,638 | 51.1 / 51.1 (lf 0.80) | 46.9 / 46.9 (lf 0.80) | 48.1 / 48.1 (lf 0.85) | 100.1 / 100.1 (lf 0.40) | 47.1 / 47.1 (lf 0.88) | 64.5 / 64.5 (lf 0.94) |
| 104,857 | 51.2 / 51.2 (lf 0.80) | 46.9 / 46.9 (lf 0.80) | 48.1 / 48.1 (lf 0.85) | 100.0 / 100.0 (lf 0.40) | 47.1 / 47.1 (lf 0.87) | 64.2 / 64.2 (lf 0.97) |
| 1,258,291 | 68.3 / 68.3 (lf 0.60) | 49.2 / 49.2 (lf 0.60) | 64.2 / 64.2 (lf 0.64) | 66.7 / 66.7 (lf 0.60) | 47.1 / 47.1 (lf 0.87) | 64.5 / 64.5 (lf 0.94) |
| 10,000,000 | 68.8 / 68.8 (lf 0.60) | 49.2 / 49.2 (lf 0.60) | 64.6 / 64.6 (lf 0.64) | 67.1 / 67.1 (lf 0.60) | 47.1 / 47.1 (lf 0.88) | 64.3 / 64.3 (lf 0.97) |

Total MiB at the largest size (final, default max_load_factor / after max_load_factor(0.9)+rehash):

| map | final MiB | peak MiB | final MiB (mlf 0.9) | lf | lf (mlf 0.9) |
|---|---|---|---|---|---|
| absl::flat_hash_map | 656.0 | 656.0 | 656.0 | 0.596 | 0.596 |
| ankerl::unordered_dense_map | 469.5 | 469.5 | 469.5 | 0.596 | 0.596 |
| boost::unordered_flat_map | 616.0 | 616.0 | 616.0 | 0.636 | 0.636 |
| emhash::hash_map8 | 640.0 | 640.0 | 640.0 | 0.596 | 0.596 |
| sflat::flat_hash_map | 449.6 | 449.6 | 449.6 | 0.875 | 0.875 |
| std::unordered_map | 613.0 | 613.0 | 613.0 | 0.966 | 0.966 |

### small_string_fix_12__uint64_t

Heap bytes per element after inserting n keys with reserve(n) (final / peak), and load factor.

| n | absl::flat_hash_map | ankerl::unordered_dense_map | boost::unordered_flat_map | emhash::hash_map8 | sflat::flat_hash_map | std::unordered_map |
|---|---|---|---|---|---|---|
| 1,638 | 51.1 / 51.1 (lf 0.80) | 46.9 / 46.9 (lf 0.80) | 48.1 / 48.1 (lf 0.85) | 100.1 / 100.1 (lf 0.40) | 47.1 / 47.1 (lf 0.88) | 64.5 / 64.5 (lf 0.94) |
| 104,857 | 51.2 / 51.2 (lf 0.80) | 46.9 / 46.9 (lf 0.80) | 48.1 / 48.1 (lf 0.85) | 100.0 / 100.0 (lf 0.40) | 47.1 / 47.1 (lf 0.87) | 64.2 / 64.2 (lf 0.97) |
| 1,258,291 | 68.3 / 68.3 (lf 0.60) | 49.2 / 49.2 (lf 0.60) | 64.2 / 64.2 (lf 0.64) | 66.7 / 66.7 (lf 0.60) | 47.1 / 47.1 (lf 0.87) | 64.5 / 64.5 (lf 0.94) |
| 10,000,000 | 68.8 / 68.8 (lf 0.60) | 49.2 / 49.2 (lf 0.60) | 64.6 / 64.6 (lf 0.64) | 67.1 / 67.1 (lf 0.60) | 47.1 / 47.1 (lf 0.88) | 64.3 / 64.3 (lf 0.97) |

Total MiB at the largest size (final, default max_load_factor / after max_load_factor(0.9)+rehash):

| map | final MiB | peak MiB | final MiB (mlf 0.9) | lf | lf (mlf 0.9) |
|---|---|---|---|---|---|
| absl::flat_hash_map | 656.0 | 656.0 | 656.0 | 0.596 | 0.596 |
| ankerl::unordered_dense_map | 469.5 | 469.5 | 469.5 | 0.596 | 0.596 |
| boost::unordered_flat_map | 616.0 | 616.0 | 616.0 | 0.636 | 0.636 |
| emhash::hash_map8 | 640.0 | 640.0 | 640.0 | 0.596 | 0.596 |
| sflat::flat_hash_map | 449.6 | 449.6 | 449.6 | 0.875 | 0.875 |
| std::unordered_map | 613.0 | 613.0 | 613.0 | 0.966 | 0.966 |

### mid_string_max_24__uint64_t

Heap bytes per element after inserting n keys with reserve(n) (final / peak), and load factor.

| n | absl::flat_hash_map | ankerl::unordered_dense_map | boost::unordered_flat_map | emhash::hash_map8 | sflat::flat_hash_map | std::unordered_map |
|---|---|---|---|---|---|---|
| 1,638 | 51.1 / 51.1 (lf 0.80) | 46.9 / 46.9 (lf 0.80) | 48.1 / 48.1 (lf 0.85) | 100.1 / 100.1 (lf 0.40) | 47.1 / 47.1 (lf 0.88) | 64.5 / 64.5 (lf 0.94) |
| 104,857 | 51.2 / 51.2 (lf 0.80) | 46.9 / 46.9 (lf 0.80) | 48.1 / 48.1 (lf 0.85) | 100.0 / 100.0 (lf 0.40) | 47.1 / 47.1 (lf 0.87) | 64.2 / 64.2 (lf 0.97) |
| 1,258,291 | 68.3 / 68.3 (lf 0.60) | 49.2 / 49.2 (lf 0.60) | 64.2 / 64.2 (lf 0.64) | 66.7 / 66.7 (lf 0.60) | 47.1 / 47.1 (lf 0.87) | 64.5 / 64.5 (lf 0.94) |
| 10,000,000 | 68.8 / 68.8 (lf 0.60) | 49.2 / 49.2 (lf 0.60) | 64.6 / 64.6 (lf 0.64) | 67.1 / 67.1 (lf 0.60) | 47.1 / 47.1 (lf 0.88) | 64.3 / 64.3 (lf 0.97) |

Total MiB at the largest size (final, default max_load_factor / after max_load_factor(0.9)+rehash):

| map | final MiB | peak MiB | final MiB (mlf 0.9) | lf | lf (mlf 0.9) |
|---|---|---|---|---|---|
| absl::flat_hash_map | 656.0 | 656.0 | 656.0 | 0.596 | 0.596 |
| ankerl::unordered_dense_map | 469.5 | 469.5 | 469.5 | 0.596 | 0.596 |
| boost::unordered_flat_map | 616.0 | 616.0 | 616.0 | 0.636 | 0.636 |
| emhash::hash_map8 | 640.0 | 640.0 | 640.0 | 0.596 | 0.596 |
| sflat::flat_hash_map | 449.6 | 449.6 | 449.6 | 0.875 | 0.875 |
| std::unordered_map | 613.0 | 613.0 | 613.0 | 0.966 | 0.966 |

### mid_string_fix_24__uint64_t

Heap bytes per element after inserting n keys with reserve(n) (final / peak), and load factor.

| n | absl::flat_hash_map | ankerl::unordered_dense_map | boost::unordered_flat_map | emhash::hash_map8 | sflat::flat_hash_map | std::unordered_map |
|---|---|---|---|---|---|---|
| 1,638 | 51.1 / 51.1 (lf 0.80) | 46.9 / 46.9 (lf 0.80) | 48.1 / 48.1 (lf 0.85) | 100.1 / 100.1 (lf 0.40) | 47.1 / 47.1 (lf 0.88) | 64.5 / 64.5 (lf 0.94) |
| 104,857 | 51.2 / 51.2 (lf 0.80) | 46.9 / 46.9 (lf 0.80) | 48.1 / 48.1 (lf 0.85) | 100.0 / 100.0 (lf 0.40) | 47.1 / 47.1 (lf 0.87) | 64.2 / 64.2 (lf 0.97) |
| 1,258,291 | 68.3 / 68.3 (lf 0.60) | 49.2 / 49.2 (lf 0.60) | 64.2 / 64.2 (lf 0.64) | 66.7 / 66.7 (lf 0.60) | 47.1 / 47.1 (lf 0.87) | 64.5 / 64.5 (lf 0.94) |
| 10,000,000 | 68.8 / 68.8 (lf 0.60) | 49.2 / 49.2 (lf 0.60) | 64.6 / 64.6 (lf 0.64) | 67.1 / 67.1 (lf 0.60) | 47.1 / 47.1 (lf 0.88) | 64.3 / 64.3 (lf 0.97) |

Total MiB at the largest size (final, default max_load_factor / after max_load_factor(0.9)+rehash):

| map | final MiB | peak MiB | final MiB (mlf 0.9) | lf | lf (mlf 0.9) |
|---|---|---|---|---|---|
| absl::flat_hash_map | 656.0 | 656.0 | 656.0 | 0.596 | 0.596 |
| ankerl::unordered_dense_map | 469.5 | 469.5 | 469.5 | 0.596 | 0.596 |
| boost::unordered_flat_map | 616.0 | 616.0 | 616.0 | 0.636 | 0.636 |
| emhash::hash_map8 | 640.0 | 640.0 | 640.0 | 0.596 | 0.596 |
| sflat::flat_hash_map | 449.6 | 449.6 | 449.6 | 0.875 | 0.875 |
| std::unordered_map | 613.0 | 613.0 | 613.0 | 0.966 | 0.966 |

### long_string_max_64__uint64_t

Heap bytes per element after inserting n keys with reserve(n) (final / peak), and load factor.

| n | absl::flat_hash_map | ankerl::unordered_dense_map | boost::unordered_flat_map | emhash::hash_map8 | sflat::flat_hash_map | std::unordered_map |
|---|---|---|---|---|---|---|
| 1,638 | 51.1 / 51.1 (lf 0.80) | 46.9 / 46.9 (lf 0.80) | 48.1 / 48.1 (lf 0.85) | 100.1 / 100.1 (lf 0.40) | 47.1 / 47.1 (lf 0.88) | 64.5 / 64.5 (lf 0.94) |
| 104,857 | 51.2 / 51.2 (lf 0.80) | 46.9 / 46.9 (lf 0.80) | 48.1 / 48.1 (lf 0.85) | 100.0 / 100.0 (lf 0.40) | 47.1 / 47.1 (lf 0.87) | 64.2 / 64.2 (lf 0.97) |
| 1,258,291 | 68.3 / 68.3 (lf 0.60) | 49.2 / 49.2 (lf 0.60) | 64.2 / 64.2 (lf 0.64) | 66.7 / 66.7 (lf 0.60) | 47.1 / 47.1 (lf 0.87) | 64.5 / 64.5 (lf 0.94) |
| 10,000,000 | 68.8 / 68.8 (lf 0.60) | 49.2 / 49.2 (lf 0.60) | 64.6 / 64.6 (lf 0.64) | 67.1 / 67.1 (lf 0.60) | 47.1 / 47.1 (lf 0.88) | 64.3 / 64.3 (lf 0.97) |

Total MiB at the largest size (final, default max_load_factor / after max_load_factor(0.9)+rehash):

| map | final MiB | peak MiB | final MiB (mlf 0.9) | lf | lf (mlf 0.9) |
|---|---|---|---|---|---|
| absl::flat_hash_map | 656.0 | 656.0 | 656.0 | 0.596 | 0.596 |
| ankerl::unordered_dense_map | 469.5 | 469.5 | 469.5 | 0.596 | 0.596 |
| boost::unordered_flat_map | 616.0 | 616.0 | 616.0 | 0.636 | 0.636 |
| emhash::hash_map8 | 640.0 | 640.0 | 640.0 | 0.596 | 0.596 |
| sflat::flat_hash_map | 449.6 | 449.6 | 449.6 | 0.875 | 0.875 |
| std::unordered_map | 613.0 | 613.0 | 613.0 | 0.966 | 0.966 |

### long_string_fix_64__uint64_t

Heap bytes per element after inserting n keys with reserve(n) (final / peak), and load factor.

| n | absl::flat_hash_map | ankerl::unordered_dense_map | boost::unordered_flat_map | emhash::hash_map8 | sflat::flat_hash_map | std::unordered_map |
|---|---|---|---|---|---|---|
| 1,638 | 51.1 / 51.1 (lf 0.80) | 46.9 / 46.9 (lf 0.80) | 48.1 / 48.1 (lf 0.85) | 100.1 / 100.1 (lf 0.40) | 47.1 / 47.1 (lf 0.88) | 64.5 / 64.5 (lf 0.94) |
| 104,857 | 51.2 / 51.2 (lf 0.80) | 46.9 / 46.9 (lf 0.80) | 48.1 / 48.1 (lf 0.85) | 100.0 / 100.0 (lf 0.40) | 47.1 / 47.1 (lf 0.87) | 64.2 / 64.2 (lf 0.97) |
| 1,258,291 | 68.3 / 68.3 (lf 0.60) | 49.2 / 49.2 (lf 0.60) | 64.2 / 64.2 (lf 0.64) | 66.7 / 66.7 (lf 0.60) | 47.1 / 47.1 (lf 0.87) | 64.5 / 64.5 (lf 0.94) |
| 10,000,000 | 68.8 / 68.8 (lf 0.60) | 49.2 / 49.2 (lf 0.60) | 64.6 / 64.6 (lf 0.64) | 67.1 / 67.1 (lf 0.60) | 47.1 / 47.1 (lf 0.88) | 64.3 / 64.3 (lf 0.97) |

Total MiB at the largest size (final, default max_load_factor / after max_load_factor(0.9)+rehash):

| map | final MiB | peak MiB | final MiB (mlf 0.9) | lf | lf (mlf 0.9) |
|---|---|---|---|---|---|
| absl::flat_hash_map | 656.0 | 656.0 | 656.0 | 0.596 | 0.596 |
| ankerl::unordered_dense_map | 469.5 | 469.5 | 469.5 | 0.596 | 0.596 |
| boost::unordered_flat_map | 616.0 | 616.0 | 616.0 | 0.636 | 0.636 |
| emhash::hash_map8 | 640.0 | 640.0 | 640.0 | 0.596 | 0.596 |
| sflat::flat_hash_map | 449.6 | 449.6 | 449.6 | 0.875 | 0.875 |
| std::unordered_map | 613.0 | 613.0 | 613.0 | 0.966 | 0.966 |

