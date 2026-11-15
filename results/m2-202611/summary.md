## Throughput

### mask_split_bits_uint64_t__uint64_t

| n=1,024 ns/op | absl::flat_hash_map | ankerl::unordered_dense_map | boost::unordered_flat_map | emhash::hash_map8 | sflat::flat_hash_map | std::unordered_map |
|---|---|---|---|---|---|---|
| insert (reserve) | 146 | 4.7 | **3.5** | 311 | 3.5 | 139 |
| insert (no reserve) | 228 | **12.5** | 16.9 | 514 | 18.1 | 23.3 |
| erase+insert | 323 | 4.9 | **4.0** | 1561 | 20.5 | 483 |
| find hit | 126 | 2.1 | **2.0** | 300 | 2.4 | 128 |
| find miss | 88.9 | **1.8** | 1.9 | 504 | 2.3 | 245 |
| find 50% | 113 | 1.7 | **1.7** | 405 | 2.2 | 191 |
| find hit (mlf 0.9) | 127 | 2.1 | **2.0** | 300 | 2.5 | 128 |
| find miss (mlf 0.9) | 89.0 | **1.8** | 1.9 | 504 | 3.3 | 245 |
| iterate | 2.3 | 0.9 | 1.6 | **0.5** | 2.3 | 1.9 |

| n=100,000 ns/op | absl::flat_hash_map | ankerl::unordered_dense_map | boost::unordered_flat_map | emhash::hash_map8 | sflat::flat_hash_map | std::unordered_map |
|---|---|---|---|---|---|---|
| insert (reserve) | 0.0 | 5.5 | **4.0** | 0.0 | 4.7 | 0.0 |
| insert (no reserve) | 0.0 | **8.7** | 11.2 | 0.0 | 11.6 | 0.0 |
| erase+insert | 0.0 | **11.2** | 15.4 | 0.0 | 25.3 | 0.0 |
| find hit | 0.0 | 3.5 | **3.3** | 0.0 | 4.0 | 0.0 |
| find miss | 0.0 | 3.3 | **3.2** | 0.0 | 4.2 | 0.0 |
| find 50% | 0.0 | **10.0** | 10.5 | 0.0 | 10.9 | 0.0 |
| find hit (mlf 0.9) | 0.0 | 3.5 | **3.4** | 0.0 | 4.1 | 0.0 |
| find miss (mlf 0.9) | 0.0 | 3.3 | **3.2** | 0.0 | 4.4 | 0.0 |
| iterate | 0.0 | **0.9** | 1.5 | 0.0 | 2.7 | 0.0 |

| n=1,200,000 ns/op | absl::flat_hash_map | ankerl::unordered_dense_map | boost::unordered_flat_map | emhash::hash_map8 | sflat::flat_hash_map | std::unordered_map |
|---|---|---|---|---|---|---|
| insert (reserve) | 0.0 | 7.6 | **4.9** | 0.0 | 6.8 | 0.0 |
| insert (no reserve) | 0.0 | **12.6** | 13.6 | 0.0 | 15.4 | 0.0 |
| erase+insert | 0.0 | 36.8 | **20.6** | 0.0 | 36.8 | 0.0 |
| find hit | 0.0 | 14.7 | 8.7 | 0.0 | **8.6** | 0.0 |
| find miss | 0.0 | 3.9 | **2.8** | 0.0 | 5.0 | 0.0 |
| find 50% | 0.0 | 14.1 | **10.9** | 0.0 | 12.5 | 0.0 |
| find hit (mlf 0.9) | 0.0 | 14.7 | 8.7 | 0.0 | **7.7** | 0.0 |
| find miss (mlf 0.9) | 0.0 | 3.9 | **2.8** | 0.0 | 5.1 | 0.0 |
| iterate | 0.0 | **0.5** | 2.3 | 0.0 | 2.8 | 0.0 |

| n=10,000,000 ns/op | absl::flat_hash_map | ankerl::unordered_dense_map | boost::unordered_flat_map | emhash::hash_map8 | sflat::flat_hash_map | std::unordered_map |
|---|---|---|---|---|---|---|
| insert (reserve) | 0.0 | 26.2 | 10.1 | 0.0 | **10.1** | 0.0 |
| insert (no reserve) | 0.0 | 31.9 | **17.9** | 0.0 | 19.1 | 0.0 |
| erase+insert | 0.0 | 62.3 | **30.7** | 0.0 | 51.4 | 0.0 |
| find hit | 0.0 | 24.4 | **14.6** | 0.0 | 16.1 | 0.0 |
| find miss | 0.0 | 14.6 | **5.5** | 0.0 | 11.3 | 0.0 |
| find 50% | 0.0 | 24.5 | **17.3** | 0.0 | 19.4 | 0.0 |
| find hit (mlf 0.9) | 0.0 | 24.4 | **14.6** | 0.0 | 16.0 | 0.0 |
| find miss (mlf 0.9) | 0.0 | 14.6 | **5.5** | 0.0 | 11.1 | 0.0 |
| iterate | 0.0 | **0.6** | 2.2 | 0.0 | 2.8 | 0.0 |

### uniform_uint64_t__uint64_t

| n=1,024 ns/op | absl::flat_hash_map | ankerl::unordered_dense_map | boost::unordered_flat_map | emhash::hash_map8 | sflat::flat_hash_map | std::unordered_map |
|---|---|---|---|---|---|---|
| insert (reserve) | 4.1 | 4.2 | **3.3** | 3.7 | 4.5 | 12.5 |
| insert (no reserve) | 12.6 | **11.7** | 14.6 | 14.3 | 19.4 | 23.4 |
| erase+insert | 14.5 | 5.0 | **4.0** | 9.6 | 20.8 | 17.0 |
| find hit | 1.8 | 2.2 | 2.0 | **1.5** | 2.5 | 2.2 |
| find miss | 1.9 | 1.7 | 1.8 | **1.3** | 2.5 | 1.8 |
| find 50% | 1.6 | 1.7 | 1.7 | **1.5** | 2.7 | 2.1 |
| find hit (mlf 0.9) | 1.8 | 2.2 | 2.0 | **1.5** | 2.6 | 2.2 |
| find miss (mlf 0.9) | 1.9 | 1.7 | 1.8 | **1.3** | 2.4 | 1.8 |
| iterate | 2.4 | 0.9 | 1.8 | **0.5** | 2.3 | 1.9 |

| n=100,000 ns/op | absl::flat_hash_map | ankerl::unordered_dense_map | boost::unordered_flat_map | emhash::hash_map8 | sflat::flat_hash_map | std::unordered_map |
|---|---|---|---|---|---|---|
| insert (reserve) | 6.0 | 5.5 | **4.1** | 10.7 | 4.8 | 19.1 |
| insert (no reserve) | 10.7 | **8.6** | 11.3 | 21.1 | 11.6 | 29.7 |
| erase+insert | 26.7 | **11.3** | 15.3 | 17.8 | 25.5 | 45.9 |
| find hit | **2.9** | 3.5 | 3.4 | 5.4 | 4.5 | 10.3 |
| find miss | 8.5 | **3.4** | 3.4 | 6.4 | 4.1 | 14.8 |
| find 50% | 10.8 | 10.1 | 10.5 | **10.0** | 11.0 | 17.7 |
| find hit (mlf 0.9) | **3.0** | 3.5 | 3.4 | 5.5 | 4.4 | 10.2 |
| find miss (mlf 0.9) | 8.6 | **3.4** | 3.4 | 6.4 | 4.1 | 15.0 |
| iterate | 3.6 | 0.9 | 1.5 | **0.5** | 2.8 | 3.6 |

| n=1,200,000 ns/op | absl::flat_hash_map | ankerl::unordered_dense_map | boost::unordered_flat_map | emhash::hash_map8 | sflat::flat_hash_map | std::unordered_map |
|---|---|---|---|---|---|---|
| insert (reserve) | 10.9 | 7.8 | **4.9** | 15.7 | 6.9 | 47.2 |
| insert (no reserve) | 14.6 | **12.8** | 13.7 | 33.8 | 15.4 | 79.4 |
| erase+insert | 32.1 | 36.8 | **21.3** | 37.0 | 36.9 | 209 |
| find hit | 8.4 | 14.7 | 8.6 | 12.8 | **8.1** | 27.7 |
| find miss | 3.9 | 3.9 | **2.8** | 8.0 | 5.1 | 36.9 |
| find 50% | **9.4** | 14.8 | 10.9 | 15.4 | 12.5 | 44.4 |
| find hit (mlf 0.9) | 8.6 | 14.6 | 8.6 | 12.6 | **8.0** | 27.7 |
| find miss (mlf 0.9) | 3.9 | 3.8 | **2.8** | 8.1 | 5.0 | 37.1 |
| iterate | 5.8 | 0.6 | 2.3 | **0.5** | 2.8 | 9.2 |

| n=10,000,000 ns/op | absl::flat_hash_map | ankerl::unordered_dense_map | boost::unordered_flat_map | emhash::hash_map8 | sflat::flat_hash_map | std::unordered_map |
|---|---|---|---|---|---|---|
| insert (reserve) | 14.3 | 26.0 | **10.0** | 28.3 | 10.1 | 88.3 |
| insert (no reserve) | 18.7 | 31.9 | **17.9** | 53.6 | 19.2 | 181 |
| erase+insert | 46.2 | 62.4 | **30.8** | 52.0 | 51.8 | 313 |
| find hit | **12.1** | 24.6 | 14.6 | 17.0 | 16.2 | 37.9 |
| find miss | 7.5 | 14.8 | **5.6** | 13.1 | 11.2 | 53.0 |
| find 50% | **14.7** | 24.7 | 17.3 | 19.2 | 19.8 | 63.4 |
| find hit (mlf 0.9) | **12.1** | 24.6 | 14.6 | 16.9 | 16.2 | 38.0 |
| find miss (mlf 0.9) | 7.8 | 14.8 | **5.6** | 13.2 | 11.2 | 53.2 |
| iterate | 5.6 | **0.4** | 2.2 | 0.5 | 2.8 | 20.3 |

### mask_high_bits_uint64_t__uint64_t

| n=1,024 ns/op | absl::flat_hash_map | ankerl::unordered_dense_map | boost::unordered_flat_map | emhash::hash_map8 | sflat::flat_hash_map | std::unordered_map |
|---|---|---|---|---|---|---|
| insert (reserve) | 12.0 | 4.1 | 3.1 | **1.8** | 3.1 | 8.2 |
| insert (no reserve) | 23.2 | 10.5 | 14.2 | **7.1** | 16.9 | 21.5 |
| erase+insert | 29.3 | 4.9 | **3.9** | 9.9 | 20.8 | 17.4 |
| find hit | 1.8 | 2.1 | 1.8 | **1.4** | 2.2 | 1.5 |
| find miss | 47.6 | 1.9 | 1.9 | **1.3** | 2.4 | 2.0 |
| find 50% | 25.8 | 1.7 | 1.7 | **1.3** | 2.2 | 1.9 |
| find hit (mlf 0.9) | 1.7 | 1.9 | 1.8 | **1.4** | 2.0 | 1.5 |
| find miss (mlf 0.9) | 48.2 | 1.9 | 1.8 | **1.3** | 2.5 | 2.0 |
| iterate | 2.2 | 0.9 | 1.7 | **0.5** | 2.5 | 1.9 |

| n=100,000 ns/op | absl::flat_hash_map | ankerl::unordered_dense_map | boost::unordered_flat_map | emhash::hash_map8 | sflat::flat_hash_map | std::unordered_map |
|---|---|---|---|---|---|---|
| insert (reserve) | 15.2 | 4.6 | 2.9 | **2.4** | 3.2 | 13.8 |
| insert (no reserve) | 22.8 | **7.2** | 9.5 | 10.9 | 10.3 | 25.6 |
| erase+insert | 46.1 | **10.9** | 14.4 | 17.1 | 24.8 | 47.9 |
| find hit | 2.0 | 2.7 | 2.4 | **1.7** | 2.7 | 7.0 |
| find miss | 18.0 | 2.8 | **2.3** | 3.7 | 3.4 | 12.9 |
| find 50% | 15.8 | 9.5 | 9.3 | **6.3** | 10.1 | 13.3 |
| find hit (mlf 0.9) | 2.0 | 2.7 | 2.4 | **1.7** | 3.4 | 7.1 |
| find miss (mlf 0.9) | 18.1 | 2.8 | **2.3** | 3.7 | 3.4 | 13.0 |
| iterate | 3.6 | 0.9 | 1.7 | **0.5** | 3.0 | 2.8 |

| n=1,200,000 ns/op | absl::flat_hash_map | ankerl::unordered_dense_map | boost::unordered_flat_map | emhash::hash_map8 | sflat::flat_hash_map | std::unordered_map |
|---|---|---|---|---|---|---|
| insert (reserve) | 21.1 | 7.0 | **4.5** | 5.9 | 5.6 | 37.6 |
| insert (no reserve) | 31.7 | **11.5** | 12.7 | 23.0 | 14.7 | 67.9 |
| erase+insert | 45.7 | 36.5 | **20.8** | 34.0 | 36.2 | 208 |
| find hit | 8.3 | 14.2 | 8.6 | 10.8 | **7.2** | 24.0 |
| find miss | 21.5 | 3.8 | **2.7** | 6.7 | 5.5 | 43.7 |
| find 50% | 22.5 | 13.8 | **11.5** | 11.8 | 11.6 | 39.3 |
| find hit (mlf 0.9) | 8.3 | 14.3 | 8.7 | 10.8 | **7.1** | 24.0 |
| find miss (mlf 0.9) | 21.5 | 3.8 | **2.7** | 6.7 | 4.4 | 43.5 |
| iterate | 6.5 | 0.6 | 2.3 | **0.5** | 2.9 | 5.7 |

| n=10,000,000 ns/op | absl::flat_hash_map | ankerl::unordered_dense_map | boost::unordered_flat_map | emhash::hash_map8 | sflat::flat_hash_map | std::unordered_map |
|---|---|---|---|---|---|---|
| insert (reserve) | 39.4 | 25.9 | **8.8** | 16.5 | 9.3 | 69.2 |
| insert (no reserve) | 50.5 | 30.6 | **16.1** | 38.9 | 18.4 | 155 |
| erase+insert | 67.8 | 61.8 | **30.5** | 49.0 | 48.0 | 304 |
| find hit | **10.8** | 23.6 | 14.3 | 14.8 | 14.5 | 31.3 |
| find miss | 44.9 | 14.9 | **5.5** | 11.5 | 10.5 | 56.9 |
| find 50% | 32.4 | 24.3 | 16.9 | **16.1** | 17.9 | 50.8 |
| find hit (mlf 0.9) | **10.8** | 23.9 | 14.3 | 14.8 | 14.4 | 30.9 |
| find miss (mlf 0.9) | 44.8 | 14.8 | **5.6** | 11.6 | 10.9 | 56.9 |
| iterate | 6.1 | 0.8 | 2.2 | **0.5** | 2.9 | 11.0 |

### mask_low_bits_uint64_t__uint64_t

| n=1,024 ns/op | absl::flat_hash_map | ankerl::unordered_dense_map | boost::unordered_flat_map | emhash::hash_map8 | sflat::flat_hash_map | std::unordered_map |
|---|---|---|---|---|---|---|
| insert (reserve) | 81.7 | 4.0 | **2.8** | 468 | 3.8 | 472 |
| insert (no reserve) | 149 | **11.3** | 13.0 | 877 | 18.8 | 19.5 |
| erase+insert | 159 | 5.0 | **3.9** | 3125 | 20.8 | 950 |
| find hit | 83.9 | 1.8 | **1.8** | 317 | 2.0 | 492 |
| find miss | 137 | **1.9** | 1.9 | 1242 | 2.4 | 939 |
| find 50% | 109 | 1.7 | **1.7** | 698 | 2.3 | 720 |
| find hit (mlf 0.9) | 83.6 | 1.8 | **1.8** | 318 | 2.1 | 486 |
| find miss (mlf 0.9) | 136 | **1.8** | 1.9 | 1236 | 2.5 | 936 |
| iterate | 2.3 | 0.9 | 1.6 | **0.5** | 2.3 | 1.9 |

| n=100,000 ns/op | absl::flat_hash_map | ankerl::unordered_dense_map | boost::unordered_flat_map | emhash::hash_map8 | sflat::flat_hash_map | std::unordered_map |
|---|---|---|---|---|---|---|
| insert (reserve) | 0.0 | 5.7 | **4.3** | 0.0 | 4.7 | 0.0 |
| insert (no reserve) | 0.0 | **9.0** | 11.9 | 0.0 | 10.8 | 0.0 |
| erase+insert | 0.0 | **11.5** | 26.7 | 0.0 | 25.4 | 0.0 |
| find hit | 0.0 | **3.6** | 3.8 | 0.0 | 4.1 | 0.0 |
| find miss | 0.0 | **3.8** | 3.8 | 0.0 | 4.1 | 0.0 |
| find 50% | 0.0 | **10.4** | 10.7 | 0.0 | 10.6 | 0.0 |
| find hit (mlf 0.9) | 0.0 | **3.6** | 3.7 | 0.0 | 3.9 | 0.0 |
| find miss (mlf 0.9) | 0.0 | **3.8** | 3.8 | 0.0 | 3.9 | 0.0 |
| iterate | 0.0 | **0.9** | 1.5 | 0.0 | 2.8 | 0.0 |

| n=1,200,000 ns/op | absl::flat_hash_map | ankerl::unordered_dense_map | boost::unordered_flat_map | emhash::hash_map8 | sflat::flat_hash_map | std::unordered_map |
|---|---|---|---|---|---|---|
| insert (reserve) | 0.0 | 7.6 | **5.0** | 0.0 | 6.7 | 0.0 |
| insert (no reserve) | 0.0 | **12.6** | 13.7 | 0.0 | 15.4 | 0.0 |
| erase+insert | 0.0 | 37.1 | **21.0** | 0.0 | 36.5 | 0.0 |
| find hit | 0.0 | 16.6 | 8.7 | 0.0 | **7.9** | 0.0 |
| find miss | 0.0 | 3.9 | **2.8** | 0.0 | 4.8 | 0.0 |
| find 50% | 0.0 | 14.8 | **11.1** | 0.0 | 13.0 | 0.0 |
| find hit (mlf 0.9) | 0.0 | 14.6 | 8.7 | 0.0 | **7.9** | 0.0 |
| find miss (mlf 0.9) | 0.0 | 3.8 | **2.7** | 0.0 | 4.9 | 0.0 |
| iterate | 0.0 | **0.5** | 2.3 | 0.0 | 2.9 | 0.0 |

| n=10,000,000 ns/op | absl::flat_hash_map | ankerl::unordered_dense_map | boost::unordered_flat_map | emhash::hash_map8 | sflat::flat_hash_map | std::unordered_map |
|---|---|---|---|---|---|---|
| insert (reserve) | 0.0 | 26.4 | 10.4 | 0.0 | **10.1** | 0.0 |
| insert (no reserve) | 0.0 | 31.9 | **17.8** | 0.0 | 19.4 | 0.0 |
| erase+insert | 0.0 | 62.6 | **30.8** | 0.0 | 51.2 | 0.0 |
| find hit | 0.0 | 24.7 | **14.7** | 0.0 | 16.5 | 0.0 |
| find miss | 0.0 | 14.9 | **5.7** | 0.0 | 11.0 | 0.0 |
| find 50% | 0.0 | 24.8 | **17.4** | 0.0 | 19.4 | 0.0 |
| find hit (mlf 0.9) | 0.0 | 24.6 | **14.6** | 0.0 | 16.5 | 0.0 |
| find miss (mlf 0.9) | 0.0 | 14.8 | **5.7** | 0.0 | 11.0 | 0.0 |
| iterate | 0.0 | **0.6** | 2.2 | 0.0 | 2.8 | 0.0 |

### mask_split_bits_uint64_t__56bytes_payload

| n=1,024 ns/op | absl::flat_hash_map | ankerl::unordered_dense_map | boost::unordered_flat_map | emhash::hash_map8 | sflat::flat_hash_map | std::unordered_map |
|---|---|---|---|---|---|---|
| insert (reserve) | 150 | 5.0 | **4.2** | 303 | 5.1 | 139 |
| insert (no reserve) | 224 | **12.4** | 17.5 | 515 | 20.2 | 21.5 |
| erase+insert | 321 | 6.2 | **5.4** | 1560 | 21.4 | 493 |
| find hit | 127 | 2.4 | 2.6 | 297 | **2.4** | 130 |
| find miss | 90.5 | **1.8** | 2.0 | 505 | 2.5 | 248 |
| find 50% | 113 | **1.9** | 1.9 | 406 | 2.3 | 187 |
| find hit (mlf 0.9) | 127 | **2.4** | 2.6 | 297 | 2.6 | 129 |
| find miss (mlf 0.9) | 89.4 | **1.8** | 2.0 | 504 | 2.5 | 248 |
| iterate | 2.2 | 0.9 | 1.7 | **0.5** | 2.3 | 1.9 |

| n=100,000 ns/op | absl::flat_hash_map | ankerl::unordered_dense_map | boost::unordered_flat_map | emhash::hash_map8 | sflat::flat_hash_map | std::unordered_map |
|---|---|---|---|---|---|---|
| insert (reserve) | 0.0 | **6.5** | 11.1 | 0.0 | 12.8 | 0.0 |
| insert (no reserve) | 0.0 | **10.6** | 17.8 | 0.0 | 17.7 | 0.0 |
| erase+insert | 0.0 | **17.1** | 23.5 | 0.0 | 28.9 | 0.0 |
| find hit | 0.0 | **4.1** | 6.7 | 0.0 | 4.6 | 0.0 |
| find miss | 0.0 | **3.4** | 3.6 | 0.0 | 4.2 | 0.0 |
| find 50% | 0.0 | **10.1** | 11.0 | 0.0 | 10.8 | 0.0 |
| find hit (mlf 0.9) | 0.0 | **3.9** | 6.7 | 0.0 | 4.8 | 0.0 |
| find miss (mlf 0.9) | 0.0 | **3.4** | 3.6 | 0.0 | 4.6 | 0.0 |
| iterate | 0.0 | **0.9** | 1.6 | 0.0 | 3.2 | 0.0 |

| n=1,200,000 ns/op | absl::flat_hash_map | ankerl::unordered_dense_map | boost::unordered_flat_map | emhash::hash_map8 | sflat::flat_hash_map | std::unordered_map |
|---|---|---|---|---|---|---|
| insert (reserve) | 0.0 | **10.7** | 12.6 | 0.0 | 17.1 | 0.0 |
| insert (no reserve) | 0.0 | **20.9** | 26.1 | 0.0 | 29.7 | 0.0 |
| erase+insert | 0.0 | 46.0 | **34.2** | 0.0 | 50.6 | 0.0 |
| find hit | 0.0 | 19.5 | 24.1 | 0.0 | **14.8** | 0.0 |
| find miss | 0.0 | 5.1 | **3.3** | 0.0 | 7.9 | 0.0 |
| find 50% | 0.0 | 17.3 | 18.7 | 0.0 | **16.3** | 0.0 |
| find hit (mlf 0.9) | 0.0 | 18.9 | 24.1 | 0.0 | **14.9** | 0.0 |
| find miss (mlf 0.9) | 0.0 | 5.1 | **3.3** | 0.0 | 7.9 | 0.0 |
| iterate | 0.0 | **0.6** | 2.3 | 0.0 | 3.2 | 0.0 |

| n=10,000,000 ns/op | absl::flat_hash_map | ankerl::unordered_dense_map | boost::unordered_flat_map | emhash::hash_map8 | sflat::flat_hash_map | std::unordered_map |
|---|---|---|---|---|---|---|
| insert (reserve) | 0.0 | 32.9 | **18.0** | 0.0 | 21.7 | 0.0 |
| insert (no reserve) | 0.0 | 41.7 | **28.6** | 0.0 | 35.8 | 0.0 |
| erase+insert | 0.0 | 0.0 | **41.6** | 0.0 | 60.6 | 0.0 |
| find hit | 0.0 | 24.1 | 31.2 | 0.0 | **21.1** | 0.0 |
| find miss | 0.0 | 14.7 | **7.0** | 0.0 | 12.0 | 0.0 |
| find 50% | 0.0 | 25.3 | 26.7 | 0.0 | **22.4** | 0.0 |
| find hit (mlf 0.9) | 0.0 | 24.1 | 31.4 | 0.0 | **21.2** | 0.0 |
| find miss (mlf 0.9) | 0.0 | 14.7 | **7.0** | 0.0 | 12.0 | 0.0 |
| iterate | 0.0 | **0.4** | 2.2 | 0.0 | 2.9 | 0.0 |

### small_string_max_12__uint64_t

| n=1,024 ns/op | absl::flat_hash_map | ankerl::unordered_dense_map | boost::unordered_flat_map | emhash::hash_map8 | sflat::flat_hash_map | std::unordered_map |
|---|---|---|---|---|---|---|
| insert (reserve) | 8.6 | 8.2 | **7.9** | 10.4 | 12.8 | 18.5 |
| insert (no reserve) | 29.3 | **19.8** | 27.2 | 34.2 | 40.8 | 29.3 |
| erase+insert | 27.4 | 17.1 | **14.7** | 28.6 | 49.2 | 29.9 |
| find hit | 9.1 | 7.4 | 7.1 | **6.6** | 8.3 | 8.1 |
| find miss | 3.5 | 3.8 | 3.9 | **3.0** | 5.0 | 4.3 |
| find 50% | 5.7 | 5.9 | 5.7 | **5.0** | 6.0 | 6.1 |
| find hit (mlf 0.9) | 7.6 | 7.3 | 7.0 | **6.7** | 7.7 | 8.4 |
| find miss (mlf 0.9) | 3.5 | 4.1 | 3.7 | **3.0** | 4.6 | 4.2 |
| iterate | 2.4 | 0.9 | 1.8 | **0.5** | 2.3 | 1.9 |

| n=100,000 ns/op | absl::flat_hash_map | ankerl::unordered_dense_map | boost::unordered_flat_map | emhash::hash_map8 | sflat::flat_hash_map | std::unordered_map |
|---|---|---|---|---|---|---|
| insert (reserve) | 11.6 | 11.9 | **11.0** | 27.2 | 14.4 | 29.5 |
| insert (no reserve) | 25.2 | **19.8** | 24.2 | 50.4 | 28.2 | 40.7 |
| erase+insert | 51.2 | **29.1** | 36.0 | 43.7 | 61.7 | 62.4 |
| find hit | **16.0** | 16.2 | 16.5 | 20.7 | 17.9 | 27.9 |
| find miss | 17.2 | **10.3** | 10.6 | 15.9 | 11.0 | 26.8 |
| find 50% | 24.5 | 23.8 | **23.7** | 25.7 | 24.1 | 35.1 |
| find hit (mlf 0.9) | **15.8** | 16.5 | 16.7 | 20.6 | 17.8 | 28.1 |
| find miss (mlf 0.9) | 17.5 | **10.3** | 10.6 | 16.0 | 10.9 | 26.8 |
| iterate | 3.6 | 0.9 | 1.5 | **0.5** | 2.8 | 4.0 |

| n=1,200,000 ns/op | absl::flat_hash_map | ankerl::unordered_dense_map | boost::unordered_flat_map | emhash::hash_map8 | sflat::flat_hash_map | std::unordered_map |
|---|---|---|---|---|---|---|
| insert (reserve) | 18.1 | 13.5 | **11.1** | 37.4 | 18.9 | 62.5 |
| insert (no reserve) | 32.1 | **25.8** | 28.9 | 75.6 | 37.5 | 111 |
| erase+insert | 63.6 | 72.3 | **44.7** | 87.5 | 90.9 | 232 |
| find hit | **28.2** | 38.5 | 29.7 | 41.0 | 30.0 | 74.9 |
| find miss | 10.8 | 9.7 | **9.3** | 19.6 | 11.9 | 60.5 |
| find 50% | **26.1** | 31.3 | 27.8 | 36.0 | 29.5 | 76.5 |
| find hit (mlf 0.9) | **28.2** | 39.4 | 29.6 | 41.0 | 30.1 | 79.1 |
| find miss (mlf 0.9) | 10.8 | 9.6 | **9.3** | 19.6 | 11.9 | 61.3 |
| iterate | 5.9 | 0.5 | 2.3 | **0.5** | 2.8 | 15.7 |

| n=10,000,000 ns/op | absl::flat_hash_map | ankerl::unordered_dense_map | boost::unordered_flat_map | emhash::hash_map8 | sflat::flat_hash_map | std::unordered_map |
|---|---|---|---|---|---|---|
| insert (reserve) | 27.0 | 32.6 | **16.4** | 58.3 | 25.7 | 97.8 |
| insert (no reserve) | 38.9 | 44.7 | **33.8** | 110 | 45.2 | 202 |
| erase+insert | 0.0 | 0.0 | **55.0** | 112 | 108 | 291 |
| find hit | **38.3** | 59.4 | 39.4 | 51.6 | 41.2 | 92.8 |
| find miss | 16.9 | 23.0 | **12.4** | 28.6 | 17.4 | 74.3 |
| find 50% | **36.2** | 50.2 | 39.3 | 44.8 | 39.3 | 91.7 |
| find hit (mlf 0.9) | **38.4** | 59.3 | 39.1 | 51.7 | 41.3 | 92.6 |
| find miss (mlf 0.9) | 15.9 | 23.0 | **12.4** | 28.6 | 17.4 | 74.2 |
| iterate | 5.6 | **0.4** | 2.2 | 0.5 | 2.8 | 25.6 |

### small_string_fix_12__uint64_t

| n=1,024 ns/op | absl::flat_hash_map | ankerl::unordered_dense_map | boost::unordered_flat_map | emhash::hash_map8 | sflat::flat_hash_map | std::unordered_map |
|---|---|---|---|---|---|---|
| insert (reserve) | 6.0 | 6.8 | **5.6** | 11.1 | 10.7 | 17.3 |
| insert (no reserve) | 21.2 | **16.9** | 21.6 | 28.8 | 33.3 | 28.0 |
| erase+insert | 23.1 | 13.9 | **8.9** | 21.1 | 38.1 | 25.2 |
| find hit | **5.6** | 7.0 | 6.5 | 7.7 | 8.3 | 9.1 |
| find miss | 4.2 | 4.2 | 4.2 | **3.5** | 5.9 | 5.0 |
| find 50% | 5.1 | 5.8 | 7.4 | **4.3** | 6.8 | 6.6 |
| find hit (mlf 0.9) | **5.6** | 7.0 | 6.5 | 7.7 | 8.3 | 8.9 |
| find miss (mlf 0.9) | 4.4 | 4.2 | 4.2 | **3.3** | 6.1 | 4.1 |
| iterate | 2.4 | 0.9 | 1.8 | **0.5** | 2.3 | 1.9 |

| n=100,000 ns/op | absl::flat_hash_map | ankerl::unordered_dense_map | boost::unordered_flat_map | emhash::hash_map8 | sflat::flat_hash_map | std::unordered_map |
|---|---|---|---|---|---|---|
| insert (reserve) | **8.5** | 8.9 | 8.5 | 22.2 | 13.0 | 26.4 |
| insert (no reserve) | 18.2 | **13.7** | 18.6 | 40.2 | 22.7 | 37.7 |
| erase+insert | 43.0 | **24.2** | 25.4 | 32.7 | 45.3 | 58.8 |
| find hit | **8.7** | 9.8 | 9.5 | 13.4 | 10.2 | 20.6 |
| find miss | 14.7 | 6.9 | **6.8** | 13.8 | 7.5 | 24.6 |
| find 50% | 21.0 | **19.3** | 19.6 | 21.9 | 20.1 | 29.7 |
| find hit (mlf 0.9) | **8.7** | 9.8 | 9.4 | 13.4 | 10.3 | 20.6 |
| find miss (mlf 0.9) | 14.7 | 6.9 | **6.8** | 13.8 | 7.6 | 24.4 |
| iterate | 3.6 | 0.9 | 1.5 | **0.5** | 2.8 | 4.0 |

| n=1,200,000 ns/op | absl::flat_hash_map | ankerl::unordered_dense_map | boost::unordered_flat_map | emhash::hash_map8 | sflat::flat_hash_map | std::unordered_map |
|---|---|---|---|---|---|---|
| insert (reserve) | 24.8 | **14.5** | 21.9 | 39.0 | 27.1 | 60.5 |
| insert (no reserve) | 27.7 | **20.8** | 24.0 | 62.9 | 31.1 | 110 |
| erase+insert | 60.2 | 69.5 | **40.6** | 78.8 | 78.5 | 227 |
| find hit | **25.6** | 38.6 | 26.8 | 38.3 | 27.1 | 68.8 |
| find miss | 7.8 | 7.3 | **5.9** | 17.1 | 8.8 | 58.4 |
| find 50% | **23.8** | 29.0 | 25.3 | 32.5 | 26.6 | 71.9 |
| find hit (mlf 0.9) | **25.9** | 33.6 | 26.6 | 37.5 | 27.0 | 68.9 |
| find miss (mlf 0.9) | 7.8 | 7.3 | **5.9** | 17.1 | 8.9 | 58.6 |
| iterate | 5.9 | 0.5 | 2.3 | **0.5** | 2.8 | 15.8 |

| n=10,000,000 ns/op | absl::flat_hash_map | ankerl::unordered_dense_map | boost::unordered_flat_map | emhash::hash_map8 | sflat::flat_hash_map | std::unordered_map |
|---|---|---|---|---|---|---|
| insert (reserve) | 28.7 | 32.0 | **18.6** | 52.8 | 25.2 | 95.9 |
| insert (no reserve) | 30.3 | 40.5 | **27.7** | 95.7 | 38.2 | 199 |
| erase+insert | 77.4 | 94.9 | **50.9** | 105 | 95.4 | 287 |
| find hit | 35.8 | 54.3 | **35.8** | 48.9 | 37.9 | 84.8 |
| find miss | 14.9 | 23.9 | **10.4** | 26.9 | 15.9 | 71.5 |
| find 50% | **32.4** | 46.9 | 46.6 | 40.8 | 35.5 | 85.2 |
| find hit (mlf 0.9) | **35.8** | 54.2 | 36.1 | 49.0 | 38.0 | 84.4 |
| find miss (mlf 0.9) | 14.5 | 22.7 | **10.8** | 26.9 | 15.8 | 71.1 |
| iterate | 5.6 | **0.5** | 2.2 | 0.5 | 2.8 | 24.0 |

### mid_string_max_24__uint64_t

| n=1,024 ns/op | absl::flat_hash_map | ankerl::unordered_dense_map | boost::unordered_flat_map | emhash::hash_map8 | sflat::flat_hash_map | std::unordered_map |
|---|---|---|---|---|---|---|
| insert (reserve) | 11.1 | 10.7 | **9.9** | 14.4 | 16.2 | 21.4 |
| insert (no reserve) | 37.1 | **26.4** | 30.5 | 49.1 | 51.0 | 36.9 |
| erase+insert | 30.9 | 21.2 | **17.6** | 33.2 | 56.0 | 34.3 |
| find hit | 8.5 | 7.8 | 7.5 | 7.5 | 7.9 | **7.4** |
| find miss | 3.9 | 4.5 | 4.7 | **3.5** | 5.2 | 4.4 |
| find 50% | 5.9 | 6.7 | 6.1 | **5.1** | 6.6 | 5.9 |
| find hit (mlf 0.9) | 7.1 | 8.0 | 7.6 | **6.8** | 7.6 | 7.5 |
| find miss (mlf 0.9) | 3.9 | 4.5 | 4.9 | **3.4** | 5.2 | 4.4 |
| iterate | 2.4 | 0.9 | 1.8 | **0.5** | 2.3 | 1.9 |

| n=100,000 ns/op | absl::flat_hash_map | ankerl::unordered_dense_map | boost::unordered_flat_map | emhash::hash_map8 | sflat::flat_hash_map | std::unordered_map |
|---|---|---|---|---|---|---|
| insert (reserve) | 14.5 | 14.7 | **13.9** | 31.3 | 17.6 | 32.6 |
| insert (no reserve) | 30.2 | **24.1** | 28.1 | 57.4 | 36.6 | 43.4 |
| erase+insert | 58.3 | **35.3** | 42.3 | 51.0 | 71.3 | 68.8 |
| find hit | **16.5** | 17.0 | 17.8 | 21.3 | 18.7 | 28.8 |
| find miss | 19.0 | **11.9** | 12.2 | 17.5 | 12.6 | 28.7 |
| find 50% | 25.9 | **25.1** | 25.4 | 27.0 | 25.6 | 37.0 |
| find hit (mlf 0.9) | **16.6** | 17.0 | 17.8 | 21.3 | 18.7 | 28.7 |
| find miss (mlf 0.9) | 18.9 | **11.9** | 12.2 | 17.5 | 12.5 | 28.6 |
| iterate | 3.6 | 0.9 | 1.5 | **0.5** | 2.8 | 4.0 |

| n=1,200,000 ns/op | absl::flat_hash_map | ankerl::unordered_dense_map | boost::unordered_flat_map | emhash::hash_map8 | sflat::flat_hash_map | std::unordered_map |
|---|---|---|---|---|---|---|
| insert (reserve) | 19.9 | **17.1** | 19.7 | 44.3 | 21.8 | 68.3 |
| insert (no reserve) | 38.1 | **30.7** | 34.0 | 88.2 | 48.6 | 117 |
| erase+insert | 77.7 | 89.9 | **60.6** | 109 | 116 | 251 |
| find hit | 39.2 | 48.6 | **38.9** | 50.5 | 38.9 | 82.3 |
| find miss | 12.6 | 12.3 | **10.9** | 23.9 | 14.2 | 66.4 |
| find 50% | **32.9** | 40.7 | 34.7 | 42.8 | 35.6 | 82.1 |
| find hit (mlf 0.9) | **37.3** | 48.9 | 39.0 | 50.1 | 39.0 | 81.4 |
| find miss (mlf 0.9) | 12.6 | 12.3 | **11.0** | 22.7 | 15.8 | 66.3 |
| iterate | 5.9 | 0.5 | 2.3 | **0.5** | 2.8 | 15.7 |

| n=10,000,000 ns/op | absl::flat_hash_map | ankerl::unordered_dense_map | boost::unordered_flat_map | emhash::hash_map8 | sflat::flat_hash_map | std::unordered_map |
|---|---|---|---|---|---|---|
| insert (reserve) | **23.5** | 39.5 | 24.4 | 66.5 | 28.3 | 104 |
| insert (no reserve) | 43.7 | 48.2 | **40.6** | 127 | 58.2 | 209 |
| erase+insert | 98.0 | 0.0 | **73.9** | 137 | 143 | 312 |
| find hit | **50.7** | 72.5 | 52.5 | 63.0 | 53.5 | 99.9 |
| find miss | 21.4 | 28.7 | **17.8** | 34.4 | 22.5 | 81.3 |
| find 50% | **44.4** | 59.4 | 48.0 | 54.4 | 47.6 | 99.5 |
| find hit (mlf 0.9) | **50.8** | 72.4 | 51.3 | 63.2 | 53.1 | 100 |
| find miss (mlf 0.9) | 21.2 | 28.9 | **17.8** | 34.4 | 22.5 | 81.9 |
| iterate | 5.6 | 0.6 | 2.2 | **0.5** | 2.8 | 24.0 |

### mid_string_fix_24__uint64_t

| n=1,024 ns/op | absl::flat_hash_map | ankerl::unordered_dense_map | boost::unordered_flat_map | emhash::hash_map8 | sflat::flat_hash_map | std::unordered_map |
|---|---|---|---|---|---|---|
| insert (reserve) | **14.8** | 15.8 | 15.1 | 22.0 | 32.0 | 28.4 |
| insert (no reserve) | **32.4** | 36.8 | 32.8 | 55.1 | 74.5 | 42.2 |
| erase+insert | 49.0 | 37.3 | **32.6** | 38.6 | 83.1 | 46.5 |
| find hit | **9.4** | 10.6 | 10.7 | 9.5 | 10.9 | 11.4 |
| find miss | 6.7 | 5.9 | 6.0 | **5.3** | 7.3 | 6.7 |
| find 50% | 9.1 | 9.7 | 9.6 | **6.3** | 10.4 | 7.2 |
| find hit (mlf 0.9) | 9.8 | 11.1 | 10.8 | **9.6** | 11.7 | 11.0 |
| find miss (mlf 0.9) | 6.5 | 5.9 | 6.0 | **5.3** | 7.5 | 5.4 |
| iterate | 2.4 | 0.9 | 1.5 | **0.5** | 2.5 | 1.9 |

| n=100,000 ns/op | absl::flat_hash_map | ankerl::unordered_dense_map | boost::unordered_flat_map | emhash::hash_map8 | sflat::flat_hash_map | std::unordered_map |
|---|---|---|---|---|---|---|
| insert (reserve) | 20.6 | 19.3 | **17.9** | 33.7 | 34.5 | 38.1 |
| insert (no reserve) | 30.3 | **24.8** | 29.7 | 54.9 | 76.0 | 48.9 |
| erase+insert | 125 | 99.5 | 122 | **82.6** | 161 | 118 |
| find hit | 18.4 | 21.1 | 18.7 | **17.6** | 19.4 | 25.4 |
| find miss | 16.8 | 9.7 | **9.7** | 16.0 | 10.5 | 27.6 |
| find 50% | 24.9 | 23.9 | **23.0** | 24.3 | 24.1 | 34.3 |
| find hit (mlf 0.9) | 18.2 | 20.9 | 18.7 | **17.9** | 19.5 | 25.3 |
| find miss (mlf 0.9) | 16.8 | 9.8 | **9.7** | 15.9 | 10.4 | 27.6 |
| iterate | 3.6 | 0.9 | 1.5 | **0.5** | 3.0 | 4.0 |

| n=1,200,000 ns/op | absl::flat_hash_map | ankerl::unordered_dense_map | boost::unordered_flat_map | emhash::hash_map8 | sflat::flat_hash_map | std::unordered_map |
|---|---|---|---|---|---|---|
| insert (reserve) | 34.5 | 26.5 | **22.6** | 77.3 | 40.5 | 86.0 |
| insert (no reserve) | 62.5 | **39.4** | 55.0 | 126 | 149 | 139 |
| erase+insert | 235 | 260 | **225** | 340 | 342 | 473 |
| find hit | **70.4** | 98.5 | 75.0 | 89.3 | 75.3 | 117 |
| find miss | 32.8 | 35.5 | **31.0** | 35.1 | 40.0 | 85.8 |
| find 50% | **62.0** | 75.3 | 64.9 | 72.4 | 66.8 | 106 |
| find hit (mlf 0.9) | **69.9** | 97.8 | 75.1 | 89.2 | 74.4 | 117 |
| find miss (mlf 0.9) | 30.7 | 33.7 | **28.5** | 34.7 | 36.9 | 85.7 |
| iterate | 5.9 | 0.6 | 2.3 | **0.5** | 2.8 | 16.5 |

| n=10,000,000 ns/op | absl::flat_hash_map | ankerl::unordered_dense_map | boost::unordered_flat_map | emhash::hash_map8 | sflat::flat_hash_map | std::unordered_map |
|---|---|---|---|---|---|---|
| insert (reserve) | 46.6 | 73.1 | **34.5** | 116 | 49.0 | 133 |
| insert (no reserve) | 83.7 | 79.1 | **77.3** | 198 | 236 | 248 |
| erase+insert | 295 | 0.0 | **263** | 0.0 | 413 | 0.0 |
| find hit | **86.2** | 115 | 87.4 | 97.8 | 91.8 | 134 |
| find miss | 41.9 | 49.2 | **39.9** | 47.9 | 49.0 | 103 |
| find 50% | **75.4** | 94.2 | 80.1 | 82.4 | 81.6 | 122 |
| find hit (mlf 0.9) | **86.2** | 115 | 87.1 | 97.6 | 92.5 | 134 |
| find miss (mlf 0.9) | 41.8 | 49.7 | **39.6** | 47.9 | 49.1 | 103 |
| iterate | 5.6 | 0.6 | 2.2 | **0.5** | 2.8 | 24.0 |

### long_string_max_64__uint64_t

| n=1,024 ns/op | absl::flat_hash_map | ankerl::unordered_dense_map | boost::unordered_flat_map | emhash::hash_map8 | sflat::flat_hash_map | std::unordered_map |
|---|---|---|---|---|---|---|
| insert (reserve) | 22.8 | 21.3 | **21.2** | 28.8 | 36.2 | 33.3 |
| insert (no reserve) | 44.5 | **34.8** | 43.5 | 60.4 | 94.0 | 45.3 |
| erase+insert | 46.5 | 36.4 | **31.0** | 53.4 | 84.1 | 48.7 |
| find hit | 9.9 | 10.5 | 10.2 | 9.5 | 9.8 | **8.8** |
| find miss | 5.9 | 5.2 | 5.1 | **4.4** | 6.6 | 5.2 |
| find 50% | 8.3 | 8.6 | 8.3 | 7.7 | 8.6 | **7.5** |
| find hit (mlf 0.9) | 10.5 | 10.2 | 10.1 | 10.2 | 9.7 | **9.2** |
| find miss (mlf 0.9) | 5.6 | 5.4 | 5.4 | **4.4** | 6.6 | 5.2 |
| iterate | 2.4 | 0.9 | 1.8 | **0.5** | 2.4 | 1.9 |

| n=100,000 ns/op | absl::flat_hash_map | ankerl::unordered_dense_map | boost::unordered_flat_map | emhash::hash_map8 | sflat::flat_hash_map | std::unordered_map |
|---|---|---|---|---|---|---|
| insert (reserve) | 26.1 | 25.7 | **25.2** | 45.3 | 37.5 | 44.7 |
| insert (no reserve) | 44.3 | **36.1** | 41.9 | 74.1 | 85.4 | 57.2 |
| erase+insert | 96.7 | **74.8** | 85.1 | 105 | 128 | 111 |
| find hit | **18.6** | 20.1 | 19.8 | 26.0 | 20.6 | 32.2 |
| find miss | 21.2 | **13.6** | 13.9 | 20.0 | 14.4 | 32.0 |
| find 50% | 28.7 | **27.7** | 27.9 | 30.7 | 28.0 | 40.6 |
| find hit (mlf 0.9) | **18.7** | 19.8 | 19.9 | 26.7 | 20.7 | 31.9 |
| find miss (mlf 0.9) | 21.1 | **13.6** | 13.9 | 20.2 | 14.4 | 31.8 |
| iterate | 3.6 | 0.9 | 1.5 | **0.5** | 2.8 | 4.3 |

| n=1,200,000 ns/op | absl::flat_hash_map | ankerl::unordered_dense_map | boost::unordered_flat_map | emhash::hash_map8 | sflat::flat_hash_map | std::unordered_map |
|---|---|---|---|---|---|---|
| insert (reserve) | 33.9 | 29.6 | **26.2** | 75.8 | 40.4 | 93.5 |
| insert (no reserve) | 68.6 | **45.4** | 64.7 | 133 | 141 | 153 |
| erase+insert | 192 | 220 | **179** | 265 | 284 | 393 |
| find hit | **74.6** | 92.8 | 77.0 | 89.0 | 76.8 | 116 |
| find miss | 28.4 | 29.8 | **26.3** | 40.3 | 33.0 | 89.2 |
| find 50% | **61.1** | 70.3 | 63.4 | 72.3 | 64.4 | 108 |
| find hit (mlf 0.9) | **74.8** | 93.0 | 77.1 | 89.0 | 76.6 | 116 |
| find miss (mlf 0.9) | 28.7 | 29.8 | **26.3** | 39.8 | 32.9 | 88.7 |
| iterate | 5.9 | 0.5 | 2.3 | **0.5** | 2.8 | 19.4 |

| n=10,000,000 ns/op | absl::flat_hash_map | ankerl::unordered_dense_map | boost::unordered_flat_map | emhash::hash_map8 | sflat::flat_hash_map | std::unordered_map |
|---|---|---|---|---|---|---|
| insert (reserve) | 44.2 | 65.1 | **34.9** | 108 | 47.1 | 135 |
| insert (no reserve) | 84.6 | **73.2** | 80.2 | 197 | 194 | 254 |
| erase+insert | **234** | 0.0 | 0.0 | 320 | 0.0 | 0.0 |
| find hit | **88.6** | 112 | 89.4 | 99.3 | 90.8 | 132 |
| find miss | 38.3 | 45.3 | **36.3** | 49.8 | 41.5 | 104 |
| find 50% | **73.0** | 90.3 | 78.3 | 82.6 | 77.6 | 123 |
| find hit (mlf 0.9) | **88.7** | 112 | 89.0 | 99.2 | 91.2 | 132 |
| find miss (mlf 0.9) | 38.3 | 45.3 | **36.0** | 49.6 | 41.3 | 111 |
| iterate | 5.9 | 0.6 | 2.2 | **0.5** | 2.8 | 26.3 |

### long_string_fix_64__uint64_t

| n=1,024 ns/op | absl::flat_hash_map | ankerl::unordered_dense_map | boost::unordered_flat_map | emhash::hash_map8 | sflat::flat_hash_map | std::unordered_map |
|---|---|---|---|---|---|---|
| insert (reserve) | 16.1 | 17.0 | **15.8** | 23.5 | 33.8 | 29.6 |
| insert (no reserve) | 35.6 | **31.9** | 34.9 | 56.1 | 80.9 | 44.4 |
| erase+insert | 64.3 | 39.9 | **35.9** | 48.4 | 87.0 | 54.6 |
| find hit | **12.4** | 13.7 | 13.2 | 14.6 | 14.5 | 15.7 |
| find miss | 8.1 | **6.9** | 6.9 | 8.9 | 8.3 | 8.9 |
| find 50% | 11.0 | 11.4 | 12.5 | **9.6** | 11.5 | 10.8 |
| find hit (mlf 0.9) | **12.6** | 13.8 | 13.2 | 13.8 | 14.0 | 15.6 |
| find miss (mlf 0.9) | 8.3 | **6.9** | 6.9 | 7.9 | 8.5 | 9.0 |
| iterate | 2.4 | 0.9 | 2.0 | **0.5** | 2.4 | 1.9 |

| n=100,000 ns/op | absl::flat_hash_map | ankerl::unordered_dense_map | boost::unordered_flat_map | emhash::hash_map8 | sflat::flat_hash_map | std::unordered_map |
|---|---|---|---|---|---|---|
| insert (reserve) | 25.8 | 22.5 | **20.7** | 41.8 | 38.8 | 42.2 |
| insert (no reserve) | 35.9 | **28.7** | 33.4 | 60.2 | 86.5 | 52.3 |
| erase+insert | 208 | **125** | 152 | 142 | 197 | 172 |
| find hit | 60.9 | 28.3 | **25.5** | 28.9 | 26.5 | 41.3 |
| find miss | 21.7 | **11.0** | 11.2 | 17.1 | 11.9 | 29.9 |
| find 50% | 45.9 | 27.3 | **26.8** | 27.4 | 27.3 | 39.9 |
| find hit (mlf 0.9) | 61.0 | 28.2 | **25.8** | 28.4 | 26.4 | 40.7 |
| find miss (mlf 0.9) | 21.9 | **11.1** | 11.1 | 17.1 | 11.9 | 29.7 |
| iterate | 3.6 | 0.9 | 1.5 | **0.5** | 2.9 | 4.0 |

| n=1,200,000 ns/op | absl::flat_hash_map | ankerl::unordered_dense_map | boost::unordered_flat_map | emhash::hash_map8 | sflat::flat_hash_map | std::unordered_map |
|---|---|---|---|---|---|---|
| insert (reserve) | 39.4 | 32.2 | **27.4** | 88.2 | 46.0 | 91.8 |
| insert (no reserve) | 91.9 | **46.5** | 81.3 | 148 | 222 | 145 |
| erase+insert | 258 | 279 | **243** | 368 | 376 | 488 |
| find hit | **96.3** | 124 | 97.2 | 115 | 98.6 | 149 |
| find miss | 45.7 | 46.8 | **42.8** | 45.6 | 49.7 | 97.7 |
| find 50% | **77.0** | 93.2 | 79.2 | 87.8 | 83.7 | 122 |
| find hit (mlf 0.9) | **95.9** | 120 | 96.0 | 114 | 98.2 | 148 |
| find miss (mlf 0.9) | 42.8 | 46.5 | **42.8** | 45.4 | 49.6 | 97.0 |
| iterate | 5.9 | 0.6 | 2.3 | **0.5** | 3.0 | 16.6 |

| n=10,000,000 ns/op | absl::flat_hash_map | ankerl::unordered_dense_map | boost::unordered_flat_map | emhash::hash_map8 | sflat::flat_hash_map | std::unordered_map |
|---|---|---|---|---|---|---|
| insert (reserve) | 57.3 | 78.6 | **41.6** | 122 | 55.7 | 137 |
| insert (no reserve) | 118 | **91.7** | 103 | 223 | 287 | 250 |
| erase+insert | 0.0 | 0.0 | **287** | 0.0 | 0.0 | 0.0 |
| find hit | 114 | 134 | **111** | 132 | 114 | 167 |
| find miss | 54.2 | 60.3 | **52.4** | 56.4 | 56.6 | 116 |
| find 50% | **89.9** | 108 | 95.7 | 98.4 | 96.3 | 144 |
| find hit (mlf 0.9) | **111** | 133 | 111 | 123 | 115 | 167 |
| find miss (mlf 0.9) | 53.6 | 59.4 | **53.2** | 55.8 | 58.0 | 117 |
| iterate | 5.6 | 0.6 | 2.2 | **0.5** | 2.8 | 24.0 |

## Heap memory

### mask_split_bits_uint64_t__uint64_t

Heap bytes per element after inserting n keys with reserve(n) (final / peak), and load factor.

| n | absl::flat_hash_map | ankerl::unordered_dense_map | boost::unordered_flat_map | emhash::hash_map8 | sflat::flat_hash_map | std::unordered_map |
|---|---|---|---|---|---|---|
| 1,638 | 21.2 / 21.2 (lf 0.80) | 22.9 / 22.9 (lf 0.80) | 20.0 / 20.0 (lf 0.85) | 52.1 / 52.1 (lf 0.40) | 19.7 / 19.7 (lf 0.88) | 40.1 / 40.1 (lf 0.99) |
| 104,857 | 0.0 / 0.0 (lf 0.00) | 22.9 / 22.9 (lf 0.80) | 20.0 / 20.0 (lf 0.85) | 0.0 / 0.0 (lf 0.00) | 19.7 / 19.7 (lf 0.87) | 40.0 / 40.0 (lf 1.00) |
| 1,258,291 | 0.0 / 0.0 (lf 0.00) | 25.2 / 25.2 (lf 0.60) | 26.7 / 26.7 (lf 0.64) | 0.0 / 0.0 (lf 0.00) | 19.7 / 19.7 (lf 0.87) | 40.0 / 40.0 (lf 1.00) |
| 10,000,000 | 0.0 / 0.0 (lf 0.00) | 25.2 / 25.2 (lf 0.60) | 26.8 / 26.8 (lf 0.64) | 0.0 / 0.0 (lf 0.00) | 19.7 / 19.7 (lf 0.88) | 40.0 / 40.0 (lf 1.00) |

Total MiB at the largest size (final, default max_load_factor / after max_load_factor(0.9)+rehash):

| map | final MiB | peak MiB | final MiB (mlf 0.9) | lf | lf (mlf 0.9) |
|---|---|---|---|---|---|
| absl::flat_hash_map | 0.0 | 0.0 | 0.0 | 0.000 | 0.000 |
| ankerl::unordered_dense_map | 240.6 | 240.6 | 240.6 | 0.596 | 0.596 |
| boost::unordered_flat_map | 256.0 | 256.0 | 256.0 | 0.636 | 0.636 |
| emhash::hash_map8 | 0.0 | 0.0 | 0.0 | 0.000 | 0.000 |
| sflat::flat_hash_map | 188.0 | 188.0 | 188.0 | 0.875 | 0.875 |
| std::unordered_map | 381.5 | 381.5 | 381.5 | 1.000 | 1.000 |

### uniform_uint64_t__uint64_t

Heap bytes per element after inserting n keys with reserve(n) (final / peak), and load factor.

| n | absl::flat_hash_map | ankerl::unordered_dense_map | boost::unordered_flat_map | emhash::hash_map8 | sflat::flat_hash_map | std::unordered_map |
|---|---|---|---|---|---|---|
| 1,638 | 21.2 / 21.2 (lf 0.80) | 22.9 / 22.9 (lf 0.80) | 20.0 / 20.0 (lf 0.85) | 52.1 / 52.1 (lf 0.40) | 19.7 / 19.7 (lf 0.88) | 40.1 / 40.1 (lf 0.99) |
| 104,857 | 21.2 / 21.2 (lf 0.80) | 22.9 / 22.9 (lf 0.80) | 20.0 / 20.0 (lf 0.85) | 52.0 / 52.0 (lf 0.40) | 19.7 / 19.7 (lf 0.87) | 40.0 / 40.0 (lf 1.00) |
| 1,258,291 | 28.3 / 28.3 (lf 0.60) | 25.2 / 25.2 (lf 0.60) | 26.7 / 26.7 (lf 0.64) | 34.7 / 34.7 (lf 0.60) | 19.7 / 19.7 (lf 0.87) | 40.0 / 40.0 (lf 1.00) |
| 10,000,000 | 28.5 / 28.5 (lf 0.60) | 25.2 / 25.2 (lf 0.60) | 26.8 / 26.8 (lf 0.64) | 34.9 / 34.9 (lf 0.60) | 19.7 / 19.7 (lf 0.88) | 40.0 / 40.0 (lf 1.00) |

Total MiB at the largest size (final, default max_load_factor / after max_load_factor(0.9)+rehash):

| map | final MiB | peak MiB | final MiB (mlf 0.9) | lf | lf (mlf 0.9) |
|---|---|---|---|---|---|
| absl::flat_hash_map | 272.0 | 272.0 | 272.0 | 0.596 | 0.596 |
| ankerl::unordered_dense_map | 240.6 | 240.6 | 240.6 | 0.596 | 0.596 |
| boost::unordered_flat_map | 256.0 | 256.0 | 256.0 | 0.636 | 0.636 |
| emhash::hash_map8 | 332.8 | 332.8 | 332.8 | 0.596 | 0.596 |
| sflat::flat_hash_map | 188.0 | 188.0 | 188.0 | 0.875 | 0.875 |
| std::unordered_map | 381.5 | 381.5 | 381.5 | 1.000 | 1.000 |

### mask_high_bits_uint64_t__uint64_t

Heap bytes per element after inserting n keys with reserve(n) (final / peak), and load factor.

| n | absl::flat_hash_map | ankerl::unordered_dense_map | boost::unordered_flat_map | emhash::hash_map8 | sflat::flat_hash_map | std::unordered_map |
|---|---|---|---|---|---|---|
| 1,638 | 21.2 / 21.2 (lf 0.80) | 22.9 / 22.9 (lf 0.80) | 20.0 / 20.0 (lf 0.85) | 52.1 / 52.1 (lf 0.40) | 19.7 / 19.7 (lf 0.88) | 40.1 / 40.1 (lf 0.99) |
| 104,857 | 21.2 / 21.2 (lf 0.80) | 22.9 / 22.9 (lf 0.80) | 20.0 / 20.0 (lf 0.85) | 52.0 / 52.0 (lf 0.40) | 19.7 / 19.7 (lf 0.87) | 40.0 / 40.0 (lf 1.00) |
| 1,258,291 | 28.3 / 28.3 (lf 0.60) | 25.2 / 25.2 (lf 0.60) | 26.7 / 26.7 (lf 0.64) | 34.7 / 34.7 (lf 0.60) | 19.7 / 19.7 (lf 0.87) | 40.0 / 40.0 (lf 1.00) |
| 10,000,000 | 28.5 / 28.5 (lf 0.60) | 25.2 / 25.2 (lf 0.60) | 26.8 / 26.8 (lf 0.64) | 34.9 / 34.9 (lf 0.60) | 19.7 / 19.7 (lf 0.88) | 40.0 / 40.0 (lf 1.00) |

Total MiB at the largest size (final, default max_load_factor / after max_load_factor(0.9)+rehash):

| map | final MiB | peak MiB | final MiB (mlf 0.9) | lf | lf (mlf 0.9) |
|---|---|---|---|---|---|
| absl::flat_hash_map | 272.0 | 272.0 | 272.0 | 0.596 | 0.596 |
| ankerl::unordered_dense_map | 240.6 | 240.6 | 240.6 | 0.596 | 0.596 |
| boost::unordered_flat_map | 256.0 | 256.0 | 256.0 | 0.636 | 0.636 |
| emhash::hash_map8 | 332.8 | 332.8 | 332.8 | 0.596 | 0.596 |
| sflat::flat_hash_map | 188.0 | 188.0 | 188.0 | 0.875 | 0.875 |
| std::unordered_map | 381.5 | 381.5 | 381.5 | 1.000 | 1.000 |

### mask_low_bits_uint64_t__uint64_t

Heap bytes per element after inserting n keys with reserve(n) (final / peak), and load factor.

| n | absl::flat_hash_map | ankerl::unordered_dense_map | boost::unordered_flat_map | emhash::hash_map8 | sflat::flat_hash_map | std::unordered_map |
|---|---|---|---|---|---|---|
| 1,638 | 21.2 / 21.2 (lf 0.80) | 22.9 / 22.9 (lf 0.80) | 20.0 / 20.0 (lf 0.85) | 52.1 / 52.1 (lf 0.40) | 19.7 / 19.7 (lf 0.88) | 40.1 / 40.1 (lf 0.99) |
| 104,857 | 0.0 / 0.0 (lf 0.00) | 22.9 / 22.9 (lf 0.80) | 20.0 / 20.0 (lf 0.85) | 0.0 / 0.0 (lf 0.00) | 19.7 / 19.7 (lf 0.87) | 40.0 / 40.0 (lf 1.00) |
| 1,258,291 | 0.0 / 0.0 (lf 0.00) | 25.2 / 25.2 (lf 0.60) | 26.7 / 26.7 (lf 0.64) | 0.0 / 0.0 (lf 0.00) | 19.7 / 19.7 (lf 0.87) | 40.0 / 40.0 (lf 1.00) |
| 10,000,000 | 0.0 / 0.0 (lf 0.00) | 25.2 / 25.2 (lf 0.60) | 26.8 / 26.8 (lf 0.64) | 0.0 / 0.0 (lf 0.00) | 19.7 / 19.7 (lf 0.88) | 40.0 / 40.0 (lf 1.00) |

Total MiB at the largest size (final, default max_load_factor / after max_load_factor(0.9)+rehash):

| map | final MiB | peak MiB | final MiB (mlf 0.9) | lf | lf (mlf 0.9) |
|---|---|---|---|---|---|
| absl::flat_hash_map | 0.0 | 0.0 | 0.0 | 0.000 | 0.000 |
| ankerl::unordered_dense_map | 240.6 | 240.6 | 240.6 | 0.596 | 0.596 |
| boost::unordered_flat_map | 256.0 | 256.0 | 256.0 | 0.636 | 0.636 |
| emhash::hash_map8 | 0.0 | 0.0 | 0.0 | 0.000 | 0.000 |
| sflat::flat_hash_map | 188.0 | 188.0 | 188.0 | 0.875 | 0.875 |
| std::unordered_map | 381.5 | 381.5 | 381.5 | 1.000 | 1.000 |

### mask_split_bits_uint64_t__56bytes_payload

Heap bytes per element after inserting n keys with reserve(n) (final / peak), and load factor.

| n | absl::flat_hash_map | ankerl::unordered_dense_map | boost::unordered_flat_map | emhash::hash_map8 | sflat::flat_hash_map | std::unordered_map |
|---|---|---|---|---|---|---|
| 1,638 | 81.0 / 81.0 (lf 0.80) | 70.9 / 70.9 (lf 0.80) | 76.3 / 76.3 (lf 0.85) | 148.2 / 148.2 (lf 0.40) | 74.6 / 74.6 (lf 0.88) | 88.1 / 88.1 (lf 0.99) |
| 104,857 | 0.0 / 0.0 (lf 0.00) | 70.9 / 70.9 (lf 0.80) | 76.3 / 76.3 (lf 0.85) | 0.0 / 0.0 (lf 0.00) | 74.6 / 74.6 (lf 0.87) | 88.0 / 88.0 (lf 1.00) |
| 1,258,291 | 0.0 / 0.0 (lf 0.00) | 73.2 / 73.2 (lf 0.60) | 101.7 / 101.7 (lf 0.64) | 0.0 / 0.0 (lf 0.00) | 74.6 / 74.6 (lf 0.87) | 88.0 / 88.0 (lf 1.00) |
| 10,000,000 | 0.0 / 0.0 (lf 0.00) | 73.2 / 73.2 (lf 0.60) | 102.3 / 102.3 (lf 0.64) | 0.0 / 0.0 (lf 0.00) | 74.6 / 74.6 (lf 0.88) | 88.0 / 88.0 (lf 1.00) |

Total MiB at the largest size (final, default max_load_factor / after max_load_factor(0.9)+rehash):

| map | final MiB | peak MiB | final MiB (mlf 0.9) | lf | lf (mlf 0.9) |
|---|---|---|---|---|---|
| absl::flat_hash_map | 0.0 | 0.0 | 0.0 | 0.000 | 0.000 |
| ankerl::unordered_dense_map | 698.4 | 698.4 | 698.4 | 0.596 | 0.596 |
| boost::unordered_flat_map | 976.0 | 976.0 | 976.0 | 0.636 | 0.636 |
| emhash::hash_map8 | 0.0 | 0.0 | 0.0 | 0.000 | 0.000 |
| sflat::flat_hash_map | 711.2 | 711.2 | 711.2 | 0.875 | 0.875 |
| std::unordered_map | 839.2 | 839.2 | 839.2 | 1.000 | 1.000 |

### small_string_max_12__uint64_t

Heap bytes per element after inserting n keys with reserve(n) (final / peak), and load factor.

| n | absl::flat_hash_map | ankerl::unordered_dense_map | boost::unordered_flat_map | emhash::hash_map8 | sflat::flat_hash_map | std::unordered_map |
|---|---|---|---|---|---|---|
| 1,638 | 41.2 / 41.2 (lf 0.80) | 38.9 / 38.9 (lf 0.80) | 38.8 / 38.8 (lf 0.85) | 84.1 / 84.1 (lf 0.40) | 38.0 / 38.0 (lf 0.88) | 56.1 / 56.1 (lf 0.99) |
| 104,857 | 41.2 / 41.2 (lf 0.80) | 38.9 / 38.9 (lf 0.80) | 38.8 / 38.8 (lf 0.85) | 84.0 / 84.0 (lf 0.40) | 38.0 / 38.0 (lf 0.87) | 56.0 / 56.0 (lf 1.00) |
| 1,258,291 | 55.0 / 55.0 (lf 0.60) | 41.2 / 41.2 (lf 0.60) | 51.7 / 51.7 (lf 0.64) | 56.0 / 56.0 (lf 0.60) | 38.0 / 38.0 (lf 0.87) | 56.0 / 56.0 (lf 1.00) |
| 10,000,000 | 55.4 / 55.4 (lf 0.60) | 41.2 / 41.2 (lf 0.60) | 52.0 / 52.0 (lf 0.64) | 56.4 / 56.4 (lf 0.60) | 38.0 / 38.0 (lf 0.88) | 56.0 / 56.0 (lf 1.00) |

Total MiB at the largest size (final, default max_load_factor / after max_load_factor(0.9)+rehash):

| map | final MiB | peak MiB | final MiB (mlf 0.9) | lf | lf (mlf 0.9) |
|---|---|---|---|---|---|
| absl::flat_hash_map | 528.0 | 528.0 | 528.0 | 0.596 | 0.596 |
| ankerl::unordered_dense_map | 393.2 | 393.2 | 393.2 | 0.596 | 0.596 |
| boost::unordered_flat_map | 496.0 | 496.0 | 496.0 | 0.636 | 0.636 |
| emhash::hash_map8 | 537.6 | 537.6 | 537.6 | 0.596 | 0.596 |
| sflat::flat_hash_map | 362.4 | 362.4 | 362.4 | 0.875 | 0.875 |
| std::unordered_map | 534.1 | 534.1 | 534.1 | 1.000 | 1.000 |

### small_string_fix_12__uint64_t

Heap bytes per element after inserting n keys with reserve(n) (final / peak), and load factor.

| n | absl::flat_hash_map | ankerl::unordered_dense_map | boost::unordered_flat_map | emhash::hash_map8 | sflat::flat_hash_map | std::unordered_map |
|---|---|---|---|---|---|---|
| 1,638 | 41.2 / 41.2 (lf 0.80) | 38.9 / 38.9 (lf 0.80) | 38.8 / 38.8 (lf 0.85) | 84.1 / 84.1 (lf 0.40) | 38.0 / 38.0 (lf 0.88) | 56.1 / 56.1 (lf 0.99) |
| 104,857 | 41.2 / 41.2 (lf 0.80) | 38.9 / 38.9 (lf 0.80) | 38.8 / 38.8 (lf 0.85) | 84.0 / 84.0 (lf 0.40) | 38.0 / 38.0 (lf 0.87) | 56.0 / 56.0 (lf 1.00) |
| 1,258,291 | 55.0 / 55.0 (lf 0.60) | 41.2 / 41.2 (lf 0.60) | 51.7 / 51.7 (lf 0.64) | 56.0 / 56.0 (lf 0.60) | 38.0 / 38.0 (lf 0.87) | 56.0 / 56.0 (lf 1.00) |
| 10,000,000 | 55.4 / 55.4 (lf 0.60) | 41.2 / 41.2 (lf 0.60) | 52.0 / 52.0 (lf 0.64) | 56.4 / 56.4 (lf 0.60) | 38.0 / 38.0 (lf 0.88) | 56.0 / 56.0 (lf 1.00) |

Total MiB at the largest size (final, default max_load_factor / after max_load_factor(0.9)+rehash):

| map | final MiB | peak MiB | final MiB (mlf 0.9) | lf | lf (mlf 0.9) |
|---|---|---|---|---|---|
| absl::flat_hash_map | 528.0 | 528.0 | 528.0 | 0.596 | 0.596 |
| ankerl::unordered_dense_map | 393.2 | 393.2 | 393.2 | 0.596 | 0.596 |
| boost::unordered_flat_map | 496.0 | 496.0 | 496.0 | 0.636 | 0.636 |
| emhash::hash_map8 | 537.6 | 537.6 | 537.6 | 0.596 | 0.596 |
| sflat::flat_hash_map | 362.4 | 362.4 | 362.4 | 0.875 | 0.875 |
| std::unordered_map | 534.1 | 534.1 | 534.1 | 1.000 | 1.000 |

### mid_string_max_24__uint64_t

Heap bytes per element after inserting n keys with reserve(n) (final / peak), and load factor.

| n | absl::flat_hash_map | ankerl::unordered_dense_map | boost::unordered_flat_map | emhash::hash_map8 | sflat::flat_hash_map | std::unordered_map |
|---|---|---|---|---|---|---|
| 1,638 | 41.2 / 41.2 (lf 0.80) | 38.9 / 38.9 (lf 0.80) | 38.8 / 38.8 (lf 0.85) | 84.1 / 84.1 (lf 0.40) | 38.0 / 38.0 (lf 0.88) | 56.1 / 56.1 (lf 0.99) |
| 104,857 | 41.2 / 41.2 (lf 0.80) | 38.9 / 38.9 (lf 0.80) | 38.8 / 38.8 (lf 0.85) | 84.0 / 84.0 (lf 0.40) | 38.0 / 38.0 (lf 0.87) | 56.0 / 56.0 (lf 1.00) |
| 1,258,291 | 55.0 / 55.0 (lf 0.60) | 41.2 / 41.2 (lf 0.60) | 51.7 / 51.7 (lf 0.64) | 56.0 / 56.0 (lf 0.60) | 38.0 / 38.0 (lf 0.87) | 56.0 / 56.0 (lf 1.00) |
| 10,000,000 | 55.4 / 55.4 (lf 0.60) | 41.2 / 41.2 (lf 0.60) | 52.0 / 52.0 (lf 0.64) | 56.4 / 56.4 (lf 0.60) | 38.0 / 38.0 (lf 0.88) | 56.0 / 56.0 (lf 1.00) |

Total MiB at the largest size (final, default max_load_factor / after max_load_factor(0.9)+rehash):

| map | final MiB | peak MiB | final MiB (mlf 0.9) | lf | lf (mlf 0.9) |
|---|---|---|---|---|---|
| absl::flat_hash_map | 528.0 | 528.0 | 528.0 | 0.596 | 0.596 |
| ankerl::unordered_dense_map | 393.2 | 393.2 | 393.2 | 0.596 | 0.596 |
| boost::unordered_flat_map | 496.0 | 496.0 | 496.0 | 0.636 | 0.636 |
| emhash::hash_map8 | 537.6 | 537.6 | 537.6 | 0.596 | 0.596 |
| sflat::flat_hash_map | 362.4 | 362.4 | 362.4 | 0.875 | 0.875 |
| std::unordered_map | 534.1 | 534.1 | 534.1 | 1.000 | 1.000 |

### mid_string_fix_24__uint64_t

Heap bytes per element after inserting n keys with reserve(n) (final / peak), and load factor.

| n | absl::flat_hash_map | ankerl::unordered_dense_map | boost::unordered_flat_map | emhash::hash_map8 | sflat::flat_hash_map | std::unordered_map |
|---|---|---|---|---|---|---|
| 1,638 | 41.2 / 41.2 (lf 0.80) | 38.9 / 38.9 (lf 0.80) | 38.8 / 38.8 (lf 0.85) | 84.1 / 84.1 (lf 0.40) | 38.0 / 38.0 (lf 0.88) | 56.1 / 56.1 (lf 0.99) |
| 104,857 | 41.2 / 41.2 (lf 0.80) | 38.9 / 38.9 (lf 0.80) | 38.8 / 38.8 (lf 0.85) | 84.0 / 84.0 (lf 0.40) | 38.0 / 38.0 (lf 0.87) | 56.0 / 56.0 (lf 1.00) |
| 1,258,291 | 55.0 / 55.0 (lf 0.60) | 41.2 / 41.2 (lf 0.60) | 51.7 / 51.7 (lf 0.64) | 56.0 / 56.0 (lf 0.60) | 38.0 / 38.0 (lf 0.87) | 56.0 / 56.0 (lf 1.00) |
| 10,000,000 | 55.4 / 55.4 (lf 0.60) | 41.2 / 41.2 (lf 0.60) | 52.0 / 52.0 (lf 0.64) | 56.4 / 56.4 (lf 0.60) | 38.0 / 38.0 (lf 0.88) | 56.0 / 56.0 (lf 1.00) |

Total MiB at the largest size (final, default max_load_factor / after max_load_factor(0.9)+rehash):

| map | final MiB | peak MiB | final MiB (mlf 0.9) | lf | lf (mlf 0.9) |
|---|---|---|---|---|---|
| absl::flat_hash_map | 528.0 | 528.0 | 528.0 | 0.596 | 0.596 |
| ankerl::unordered_dense_map | 393.2 | 393.2 | 393.2 | 0.596 | 0.596 |
| boost::unordered_flat_map | 496.0 | 496.0 | 496.0 | 0.636 | 0.636 |
| emhash::hash_map8 | 537.6 | 537.6 | 537.6 | 0.596 | 0.596 |
| sflat::flat_hash_map | 362.4 | 362.4 | 362.4 | 0.875 | 0.875 |
| std::unordered_map | 534.1 | 534.1 | 534.1 | 1.000 | 1.000 |

### long_string_max_64__uint64_t

Heap bytes per element after inserting n keys with reserve(n) (final / peak), and load factor.

| n | absl::flat_hash_map | ankerl::unordered_dense_map | boost::unordered_flat_map | emhash::hash_map8 | sflat::flat_hash_map | std::unordered_map |
|---|---|---|---|---|---|---|
| 1,638 | 41.2 / 41.2 (lf 0.80) | 38.9 / 38.9 (lf 0.80) | 38.8 / 38.8 (lf 0.85) | 84.1 / 84.1 (lf 0.40) | 38.0 / 38.0 (lf 0.88) | 56.1 / 56.1 (lf 0.99) |
| 104,857 | 41.2 / 41.2 (lf 0.80) | 38.9 / 38.9 (lf 0.80) | 38.8 / 38.8 (lf 0.85) | 84.0 / 84.0 (lf 0.40) | 38.0 / 38.0 (lf 0.87) | 56.0 / 56.0 (lf 1.00) |
| 1,258,291 | 55.0 / 55.0 (lf 0.60) | 41.2 / 41.2 (lf 0.60) | 51.7 / 51.7 (lf 0.64) | 56.0 / 56.0 (lf 0.60) | 38.0 / 38.0 (lf 0.87) | 56.0 / 56.0 (lf 1.00) |
| 10,000,000 | 55.4 / 55.4 (lf 0.60) | 41.2 / 41.2 (lf 0.60) | 52.0 / 52.0 (lf 0.64) | 56.4 / 56.4 (lf 0.60) | 38.0 / 38.0 (lf 0.88) | 56.0 / 56.0 (lf 1.00) |

Total MiB at the largest size (final, default max_load_factor / after max_load_factor(0.9)+rehash):

| map | final MiB | peak MiB | final MiB (mlf 0.9) | lf | lf (mlf 0.9) |
|---|---|---|---|---|---|
| absl::flat_hash_map | 528.0 | 528.0 | 528.0 | 0.596 | 0.596 |
| ankerl::unordered_dense_map | 393.2 | 393.2 | 393.2 | 0.596 | 0.596 |
| boost::unordered_flat_map | 496.0 | 496.0 | 496.0 | 0.636 | 0.636 |
| emhash::hash_map8 | 537.6 | 537.6 | 537.6 | 0.596 | 0.596 |
| sflat::flat_hash_map | 362.4 | 362.4 | 362.4 | 0.875 | 0.875 |
| std::unordered_map | 534.1 | 534.1 | 534.1 | 1.000 | 1.000 |

### long_string_fix_64__uint64_t

Heap bytes per element after inserting n keys with reserve(n) (final / peak), and load factor.

| n | absl::flat_hash_map | ankerl::unordered_dense_map | boost::unordered_flat_map | emhash::hash_map8 | sflat::flat_hash_map | std::unordered_map |
|---|---|---|---|---|---|---|
| 1,638 | 41.2 / 41.2 (lf 0.80) | 38.9 / 38.9 (lf 0.80) | 38.8 / 38.8 (lf 0.85) | 84.1 / 84.1 (lf 0.40) | 38.0 / 38.0 (lf 0.88) | 56.1 / 56.1 (lf 0.99) |
| 104,857 | 41.2 / 41.2 (lf 0.80) | 38.9 / 38.9 (lf 0.80) | 38.8 / 38.8 (lf 0.85) | 84.0 / 84.0 (lf 0.40) | 38.0 / 38.0 (lf 0.87) | 56.0 / 56.0 (lf 1.00) |
| 1,258,291 | 55.0 / 55.0 (lf 0.60) | 41.2 / 41.2 (lf 0.60) | 51.7 / 51.7 (lf 0.64) | 56.0 / 56.0 (lf 0.60) | 38.0 / 38.0 (lf 0.87) | 56.0 / 56.0 (lf 1.00) |
| 10,000,000 | 55.4 / 55.4 (lf 0.60) | 41.2 / 41.2 (lf 0.60) | 52.0 / 52.0 (lf 0.64) | 56.4 / 56.4 (lf 0.60) | 38.0 / 38.0 (lf 0.88) | 56.0 / 56.0 (lf 1.00) |

Total MiB at the largest size (final, default max_load_factor / after max_load_factor(0.9)+rehash):

| map | final MiB | peak MiB | final MiB (mlf 0.9) | lf | lf (mlf 0.9) |
|---|---|---|---|---|---|
| absl::flat_hash_map | 528.0 | 528.0 | 528.0 | 0.596 | 0.596 |
| ankerl::unordered_dense_map | 393.2 | 393.2 | 393.2 | 0.596 | 0.596 |
| boost::unordered_flat_map | 496.0 | 496.0 | 496.0 | 0.636 | 0.636 |
| emhash::hash_map8 | 537.6 | 537.6 | 537.6 | 0.596 | 0.596 |
| sflat::flat_hash_map | 362.4 | 362.4 | 362.4 | 0.875 | 0.875 |
| std::unordered_map | 534.1 | 534.1 | 534.1 | 1.000 | 1.000 |

