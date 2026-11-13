## Throughput

### mask_split_bits_uint64_t__uint64_t

| n=1,024 ns/op | absl::flat_hash_map | ankerl::unordered_dense_map | boost::unordered_flat_map | emhash::hash_map8 | sflat::flat_hash_map | std::unordered_map |
|---|---|---|---|---|---|---|
| insert (reserve) | 844 | 34.1 | **19.5** | 1031 | 24.5 | 69.9 |
| insert (no reserve) | 1090 | 59.8 | 63.3 | 1688 | **44.6** | 107 |
| erase+insert | 964 | 39.3 | **22.2** | 3940 | 145 | 65.2 |
| find hit | 681 | 14.1 | **14.1** | 938 | 14.5 | 28.5 |
| find miss | 343 | 10.9 | **10.3** | 1372 | 15.5 | 36.0 |
| find 50% | 555 | **10.8** | 11.7 | 1161 | 12.5 | 43.0 |
| find hit (mlf 0.9) | 680 | 14.4 | **13.9** | 942 | 14.1 | 37.2 |
| find miss (mlf 0.9) | 353 | 12.4 | **10.7** | 1401 | 14.8 | 49.3 |
| iterate | 7.9 | **1.7** | 6.1 | 1.7 | 8.4 | 4.3 |

| n=100,000 ns/op | absl::flat_hash_map | ankerl::unordered_dense_map | boost::unordered_flat_map | emhash::hash_map8 | sflat::flat_hash_map | std::unordered_map |
|---|---|---|---|---|---|---|
| insert (reserve) | 0.0 | 41.2 | **31.0** | 0.0 | 40.6 | 223 |
| insert (no reserve) | 0.0 | 63.1 | **57.9** | 0.0 | 80.1 | 354 |
| erase+insert | 0.0 | 145 | **124** | 0.0 | 198 | 382 |
| find hit | 0.0 | 32.9 | **24.9** | 0.0 | 31.1 | 115 |
| find miss | 0.0 | 20.4 | **17.3** | 0.0 | 19.6 | 153 |
| find 50% | 0.0 | 45.6 | 37.7 | 0.0 | **31.5** | 187 |
| find hit (mlf 0.9) | 0.0 | 37.6 | **25.9** | 0.0 | 28.7 | 117 |
| find miss (mlf 0.9) | 0.0 | 21.1 | **17.3** | 0.0 | 20.5 | 161 |
| iterate | 0.0 | **1.6** | 5.1 | 0.0 | 7.7 | 18.5 |

| n=1,200,000 ns/op | absl::flat_hash_map | ankerl::unordered_dense_map | boost::unordered_flat_map | emhash::hash_map8 | sflat::flat_hash_map | std::unordered_map |
|---|---|---|---|---|---|---|
| insert (reserve) | 0.0 | 162 | 120 | 0.0 | **51.0** | 325 |
| insert (no reserve) | 0.0 | 171 | 154 | 0.0 | **110** | 568 |
| erase+insert | 0.0 | 310 | **214** | 0.0 | 267 | 586 |
| find hit | 0.0 | 73.5 | 55.3 | 0.0 | **45.5** | 183 |
| find miss | 0.0 | 40.4 | **24.6** | 0.0 | 27.7 | 232 |
| find 50% | 0.0 | 73.0 | 56.2 | 0.0 | **54.0** | 276 |
| find hit (mlf 0.9) | 0.0 | 71.3 | 54.7 | 0.0 | **45.4** | 175 |
| find miss (mlf 0.9) | 0.0 | 40.5 | **25.7** | 0.0 | 27.9 | 234 |
| iterate | 0.0 | **1.7** | 7.9 | 0.0 | 8.4 | 49.0 |

| n=10,000,000 ns/op | absl::flat_hash_map | ankerl::unordered_dense_map | boost::unordered_flat_map | emhash::hash_map8 | sflat::flat_hash_map | std::unordered_map |
|---|---|---|---|---|---|---|
| insert (reserve) | 0.0 | 237 | 224 | 0.0 | **67.8** | 395 |
| insert (no reserve) | 0.0 | 307 | 246 | 0.0 | **98.9** | 662 |
| erase+insert | 0.0 | 0.0 | **300** | 0.0 | 300 | 674 |
| find hit | 0.0 | 94.1 | 75.0 | 0.0 | **62.8** | 209 |
| find miss | 0.0 | 56.1 | **40.4** | 0.0 | 46.0 | 254 |
| find 50% | 0.0 | 88.5 | 78.4 | 0.0 | **73.3** | 332 |
| find hit (mlf 0.9) | 0.0 | 93.9 | 76.3 | 0.0 | **58.4** | 202 |
| find miss (mlf 0.9) | 0.0 | 53.5 | **41.3** | 0.0 | 46.7 | 262 |
| iterate | 0.0 | **1.7** | 7.9 | 0.0 | 8.3 | 62.0 |

### uniform_uint64_t__uint64_t

| n=1,024 ns/op | absl::flat_hash_map | ankerl::unordered_dense_map | boost::unordered_flat_map | emhash::hash_map8 | sflat::flat_hash_map | std::unordered_map |
|---|---|---|---|---|---|---|
| insert (reserve) | 28.9 | 31.4 | **18.8** | 24.7 | 23.5 | 148 |
| insert (no reserve) | 56.7 | **56.4** | 61.3 | 68.3 | 81.5 | 183 |
| erase+insert | 65.9 | 39.1 | **21.3** | 46.5 | 147 | 136 |
| find hit | 13.6 | 13.4 | 14.0 | **8.3** | 14.4 | 35.5 |
| find miss | 11.7 | 12.2 | 10.4 | **6.5** | 13.8 | 50.3 |
| find 50% | 11.4 | 8.6 | 10.7 | **6.7** | 13.5 | 46.1 |
| find hit (mlf 0.9) | 13.6 | 8.9 | 13.9 | **8.5** | 13.7 | 39.3 |
| find miss (mlf 0.9) | 11.5 | 11.8 | 10.4 | **6.8** | 15.4 | 52.5 |
| iterate | 7.1 | 1.7 | 6.4 | **1.6** | 8.2 | 4.6 |

| n=100,000 ns/op | absl::flat_hash_map | ankerl::unordered_dense_map | boost::unordered_flat_map | emhash::hash_map8 | sflat::flat_hash_map | std::unordered_map |
|---|---|---|---|---|---|---|
| insert (reserve) | 43.1 | 41.0 | **29.5** | 64.4 | 35.8 | 243 |
| insert (no reserve) | 65.5 | 63.0 | **59.5** | 99.3 | 97.1 | 367 |
| erase+insert | 163 | 139 | **124** | 146 | 204 | 384 |
| find hit | 26.5 | 35.3 | **26.5** | 31.9 | 28.2 | 122 |
| find miss | 27.7 | 21.0 | **17.9** | 26.6 | 20.3 | 153 |
| find 50% | 39.5 | 44.5 | **39.0** | 42.4 | 41.5 | 190 |
| find hit (mlf 0.9) | **28.0** | 35.6 | 28.8 | 33.9 | 29.4 | 123 |
| find miss (mlf 0.9) | 28.7 | 21.6 | **17.8** | 27.7 | 19.8 | 154 |
| iterate | 11.4 | **1.6** | 5.6 | 1.6 | 8.4 | 18.6 |

| n=1,200,000 ns/op | absl::flat_hash_map | ankerl::unordered_dense_map | boost::unordered_flat_map | emhash::hash_map8 | sflat::flat_hash_map | std::unordered_map |
|---|---|---|---|---|---|---|
| insert (reserve) | 138 | 164 | 124 | 103 | **48.3** | 342 |
| insert (no reserve) | 161 | 171 | 134 | 215 | **110** | 553 |
| erase+insert | **192** | 315 | 211 | 254 | 269 | 575 |
| find hit | 50.2 | 71.8 | 53.7 | 60.9 | **47.5** | 182 |
| find miss | 45.0 | 40.4 | **24.9** | 44.6 | 31.2 | 238 |
| find 50% | 60.4 | 74.6 | 55.8 | 64.3 | **54.9** | 297 |
| find hit (mlf 0.9) | 49.8 | 74.0 | 53.3 | 61.0 | **45.5** | 186 |
| find miss (mlf 0.9) | 44.4 | 43.2 | **24.7** | 45.5 | 28.3 | 237 |
| iterate | 18.0 | 1.7 | 8.0 | **1.6** | 8.2 | 51.7 |

| n=10,000,000 ns/op | absl::flat_hash_map | ankerl::unordered_dense_map | boost::unordered_flat_map | emhash::hash_map8 | sflat::flat_hash_map | std::unordered_map |
|---|---|---|---|---|---|---|
| insert (reserve) | 227 | 235 | 226 | 126 | **69.0** | 390 |
| insert (no reserve) | 244 | 308 | 245 | 301 | **111** | 659 |
| erase+insert | **293** | 0.0 | 303 | 310 | 301 | 672 |
| find hit | 81.9 | 94.2 | 82.0 | 91.0 | **63.2** | 211 |
| find miss | 75.0 | 56.3 | **40.7** | 58.6 | 46.2 | 261 |
| find 50% | 97.5 | 88.0 | 77.7 | 85.3 | **73.2** | 337 |
| find hit (mlf 0.9) | 74.5 | 92.9 | 73.8 | 99.4 | **63.1** | 213 |
| find miss (mlf 0.9) | 83.8 | 52.4 | **41.5** | 60.3 | 46.8 | 264 |
| iterate | 17.1 | 1.7 | 7.8 | **1.6** | 8.4 | 62.1 |

### mask_high_bits_uint64_t__uint64_t

| n=1,024 ns/op | absl::flat_hash_map | ankerl::unordered_dense_map | boost::unordered_flat_map | emhash::hash_map8 | sflat::flat_hash_map | std::unordered_map |
|---|---|---|---|---|---|---|
| insert (reserve) | 74.9 | 30.2 | 18.7 | **9.7** | 21.8 | 129 |
| insert (no reserve) | 121 | 54.0 | 59.6 | **37.9** | 67.8 | 166 |
| erase+insert | 122 | 37.6 | **22.3** | 41.4 | 144 | 124 |
| find hit | 12.9 | 12.8 | 13.5 | **6.6** | 14.5 | 26.9 |
| find miss | 288 | 12.1 | **10.6** | 16.0 | 14.3 | 51.8 |
| find 50% | 167 | 12.6 | 11.6 | **6.7** | 14.5 | 40.8 |
| find hit (mlf 0.9) | 13.1 | 13.5 | 13.5 | **7.2** | 13.8 | 28.2 |
| find miss (mlf 0.9) | 300 | 11.6 | **9.8** | 16.3 | 14.5 | 52.5 |
| iterate | 6.2 | 1.7 | 6.5 | **1.7** | 8.3 | 4.2 |

| n=100,000 ns/op | absl::flat_hash_map | ankerl::unordered_dense_map | boost::unordered_flat_map | emhash::hash_map8 | sflat::flat_hash_map | std::unordered_map |
|---|---|---|---|---|---|---|
| insert (reserve) | 99.1 | 37.8 | **15.3** | 19.7 | 31.6 | 161 |
| insert (no reserve) | 147 | 57.7 | **41.9** | 54.8 | 97.1 | 265 |
| erase+insert | 256 | 142 | **119** | 142 | 199 | 355 |
| find hit | 27.2 | 30.6 | **24.3** | 30.3 | 28.9 | 84.1 |
| find miss | 0.0 | 18.7 | **13.7** | 17.8 | 17.4 | 127 |
| find 50% | 81.5 | 39.9 | 34.8 | **32.3** | 38.1 | 123 |
| find hit (mlf 0.9) | 26.6 | 33.2 | **22.7** | 28.8 | 27.7 | 80.0 |
| find miss (mlf 0.9) | 0.0 | 18.2 | **14.1** | 18.0 | 17.7 | 127 |
| iterate | 11.8 | **1.6** | 5.8 | 1.7 | 8.4 | 10.9 |

| n=1,200,000 ns/op | absl::flat_hash_map | ankerl::unordered_dense_map | boost::unordered_flat_map | emhash::hash_map8 | sflat::flat_hash_map | std::unordered_map |
|---|---|---|---|---|---|---|
| insert (reserve) | 207 | 157 | 122 | **35.8** | 46.8 | 273 |
| insert (no reserve) | 271 | 175 | 136 | 175 | **105** | 456 |
| erase+insert | 303 | 312 | **210** | 258 | 259 | 548 |
| find hit | **48.0** | 70.1 | 52.7 | 57.9 | 49.7 | 146 |
| find miss | 0.0 | 40.2 | **24.0** | 41.5 | 29.6 | 212 |
| find 50% | 138 | 74.6 | 54.8 | 56.2 | **50.1** | 220 |
| find hit (mlf 0.9) | 47.6 | 73.5 | 52.6 | 54.2 | **47.1** | 147 |
| find miss (mlf 0.9) | 0.0 | 42.6 | **24.1** | 40.4 | 26.7 | 217 |
| iterate | 20.1 | **1.7** | 7.7 | 1.7 | 7.5 | 35.7 |

| n=10,000,000 ns/op | absl::flat_hash_map | ankerl::unordered_dense_map | boost::unordered_flat_map | emhash::hash_map8 | sflat::flat_hash_map | std::unordered_map |
|---|---|---|---|---|---|---|
| insert (reserve) | 261 | 235 | 227 | **62.6** | 63.2 | 310 |
| insert (no reserve) | 343 | 304 | 244 | 246 | **106** | 547 |
| erase+insert | 383 | 0.0 | 301 | 319 | **294** | 642 |
| find hit | 72.8 | 93.7 | 80.1 | 86.2 | **60.7** | 166 |
| find miss | 0.0 | 56.2 | **40.4** | 53.6 | 44.1 | 221 |
| find 50% | 171 | 88.6 | 78.8 | 79.5 | **67.8** | 242 |
| find hit (mlf 0.9) | 77.4 | 91.7 | **73.5** | 91.4 | 76.5 | 169 |
| find miss (mlf 0.9) | 0.0 | 53.9 | **40.4** | 57.6 | 42.8 | 242 |
| iterate | 19.5 | 1.7 | 7.5 | **1.6** | 7.7 | 42.2 |

### mask_low_bits_uint64_t__uint64_t

| n=1,024 ns/op | absl::flat_hash_map | ankerl::unordered_dense_map | boost::unordered_flat_map | emhash::hash_map8 | sflat::flat_hash_map | std::unordered_map |
|---|---|---|---|---|---|---|
| insert (reserve) | 184 | 29.8 | 22.1 | 0.0 | **20.8** | 120 |
| insert (no reserve) | 271 | **53.4** | 62.7 | 0.0 | 72.9 | 168 |
| erase+insert | 531 | 33.3 | **22.3** | 0.0 | 145 | 126 |
| find hit | 288 | 13.0 | 13.3 | 0.0 | **12.9** | 27.0 |
| find miss | 517 | 12.4 | **10.5** | 0.0 | 14.5 | 52.5 |
| find 50% | 406 | 12.3 | **11.5** | 0.0 | 13.9 | 42.3 |
| find hit (mlf 0.9) | 290 | **12.6** | 13.5 | 0.0 | 14.2 | 26.1 |
| find miss (mlf 0.9) | 521 | 12.3 | **10.3** | 0.0 | 14.3 | 52.7 |
| iterate | 7.3 | **1.7** | 6.4 | 0.0 | 8.4 | 4.2 |

| n=100,000 ns/op | absl::flat_hash_map | ankerl::unordered_dense_map | boost::unordered_flat_map | emhash::hash_map8 | sflat::flat_hash_map | std::unordered_map |
|---|---|---|---|---|---|---|
| insert (reserve) | 0.0 | 39.6 | **31.9** | 0.0 | 33.7 | 166 |
| insert (no reserve) | 0.0 | 63.3 | **59.3** | 0.0 | 108 | 274 |
| erase+insert | 0.0 | 137 | **128** | 0.0 | 203 | 373 |
| find hit | 0.0 | 36.0 | 27.8 | 0.0 | **27.8** | 93.5 |
| find miss | 0.0 | 22.2 | 19.0 | 0.0 | **18.6** | 140 |
| find 50% | 0.0 | 45.9 | **39.4** | 0.0 | 40.9 | 134 |
| find hit (mlf 0.9) | 0.0 | 37.2 | 29.2 | 0.0 | **26.8** | 87.2 |
| find miss (mlf 0.9) | 0.0 | 22.0 | **17.8** | 0.0 | 18.6 | 133 |
| iterate | 0.0 | **1.7** | 5.6 | 0.0 | 8.2 | 10.5 |

| n=1,200,000 ns/op | absl::flat_hash_map | ankerl::unordered_dense_map | boost::unordered_flat_map | emhash::hash_map8 | sflat::flat_hash_map | std::unordered_map |
|---|---|---|---|---|---|---|
| insert (reserve) | 0.0 | 161 | 114 | 0.0 | **46.1** | 277 |
| insert (no reserve) | 0.0 | 178 | 131 | 0.0 | **118** | 481 |
| erase+insert | 0.0 | 314 | **216** | 0.0 | 266 | 568 |
| find hit | 0.0 | 70.9 | **54.0** | 0.0 | 58.3 | 149 |
| find miss | 0.0 | 40.6 | **27.5** | 0.0 | 31.3 | 221 |
| find 50% | 0.0 | 74.9 | **55.5** | 0.0 | 58.2 | 225 |
| find hit (mlf 0.9) | 0.0 | 74.3 | 53.8 | 0.0 | **47.5** | 148 |
| find miss (mlf 0.9) | 0.0 | 43.1 | **24.2** | 0.0 | 34.1 | 222 |
| iterate | 0.0 | **1.0** | 8.1 | 0.0 | 8.3 | 35.7 |

| n=10,000,000 ns/op | absl::flat_hash_map | ankerl::unordered_dense_map | boost::unordered_flat_map | emhash::hash_map8 | sflat::flat_hash_map | std::unordered_map |
|---|---|---|---|---|---|---|
| insert (reserve) | 0.0 | 238 | 225 | 0.0 | **67.3** | 314 |
| insert (no reserve) | 0.0 | 308 | 247 | 0.0 | **125** | 558 |
| erase+insert | 0.0 | 0.0 | **300** | 0.0 | 309 | 646 |
| find hit | 0.0 | 93.4 | 75.4 | 0.0 | **61.3** | 164 |
| find miss | 0.0 | 56.8 | **41.7** | 0.0 | 46.7 | 241 |
| find 50% | 0.0 | 89.7 | 79.6 | 0.0 | **72.1** | 244 |
| find hit (mlf 0.9) | 0.0 | 96.7 | 80.9 | 0.0 | **62.8** | 161 |
| find miss (mlf 0.9) | 0.0 | 54.1 | **41.9** | 0.0 | 48.0 | 243 |
| iterate | 0.0 | **1.7** | 7.4 | 0.0 | 8.0 | 42.1 |

### mask_split_bits_uint64_t__56bytes_payload

| n=1,024 ns/op | absl::flat_hash_map | ankerl::unordered_dense_map | boost::unordered_flat_map | emhash::hash_map8 | sflat::flat_hash_map | std::unordered_map |
|---|---|---|---|---|---|---|
| insert (reserve) | 700 | 45.1 | **23.3** | 1040 | 38.2 | 143 |
| insert (no reserve) | 992 | **79.3** | 116 | 1706 | 136 | 211 |
| erase+insert | 1076 | 49.6 | **29.4** | 0.0 | 150 | 152 |
| find hit | 854 | 16.3 | **15.0** | 919 | 16.3 | 40.5 |
| find miss | 427 | 14.0 | **11.5** | 1406 | 15.4 | 55.5 |
| find 50% | 676 | 13.9 | **13.3** | 1148 | 15.4 | 45.8 |
| find hit (mlf 0.9) | 880 | 15.6 | **15.1** | 920 | 16.3 | 41.4 |
| find miss (mlf 0.9) | 428 | 14.0 | **11.5** | 1400 | 16.3 | 54.4 |
| iterate | 7.2 | **1.7** | 5.9 | 1.8 | 8.6 | 9.7 |

| n=100,000 ns/op | absl::flat_hash_map | ankerl::unordered_dense_map | boost::unordered_flat_map | emhash::hash_map8 | sflat::flat_hash_map | std::unordered_map |
|---|---|---|---|---|---|---|
| insert (reserve) | 0.0 | 74.3 | **56.1** | 0.0 | 72.0 | 274 |
| insert (no reserve) | 0.0 | 139 | **123** | 0.0 | 237 | 462 |
| erase+insert | 0.0 | **191** | 228 | 0.0 | 248 | 494 |
| find hit | 0.0 | 53.9 | 48.5 | 0.0 | **48.3** | 153 |
| find miss | 0.0 | 28.8 | **24.6** | 0.0 | 27.2 | 210 |
| find 50% | 0.0 | 57.4 | **50.7** | 0.0 | 50.9 | 247 |
| find hit (mlf 0.9) | 0.0 | 58.0 | 48.3 | 0.0 | **45.7** | 161 |
| find miss (mlf 0.9) | 0.0 | 30.0 | **24.8** | 0.0 | 26.2 | 212 |
| iterate | 0.0 | **1.7** | 5.5 | 0.0 | 8.2 | 45.6 |

| n=1,200,000 ns/op | absl::flat_hash_map | ankerl::unordered_dense_map | boost::unordered_flat_map | emhash::hash_map8 | sflat::flat_hash_map | std::unordered_map |
|---|---|---|---|---|---|---|
| insert (reserve) | 0.0 | 211 | 247 | 0.0 | **82.9** | 369 |
| insert (no reserve) | 0.0 | 364 | 378 | 0.0 | **187** | 639 |
| erase+insert | 0.0 | 0.0 | **290** | 0.0 | 310 | 666 |
| find hit | 0.0 | 88.5 | 68.6 | 0.0 | **61.7** | 206 |
| find miss | 0.0 | 51.3 | **38.9** | 0.0 | 46.1 | 263 |
| find 50% | 0.0 | 80.9 | **69.8** | 0.0 | 70.1 | 323 |
| find hit (mlf 0.9) | 0.0 | 83.6 | 68.0 | 0.0 | **62.2** | 191 |
| find miss (mlf 0.9) | 0.0 | 48.9 | **38.3** | 0.0 | 46.6 | 272 |
| iterate | 0.0 | **1.7** | 7.7 | 0.0 | 8.1 | 68.5 |

| n=10,000,000 ns/op | absl::flat_hash_map | ankerl::unordered_dense_map | boost::unordered_flat_map | emhash::hash_map8 | sflat::flat_hash_map | std::unordered_map |
|---|---|---|---|---|---|---|
| insert (reserve) | 0.0 | 251 | 389 | 0.0 | **103** | 445 |
| insert (no reserve) | 0.0 | 446 | 487 | 0.0 | **174** | 739 |
| erase+insert | 0.0 | 0.0 | 443 | 0.0 | **368** | 825 |
| find hit | 0.0 | 138 | 124 | 0.0 | **73.3** | 248 |
| find miss | 0.0 | 60.4 | **48.1** | 0.0 | 51.2 | 326 |
| find 50% | 0.0 | 137 | 107 | 0.0 | **82.9** | 406 |
| find hit (mlf 0.9) | 0.0 | 134 | 125 | 0.0 | **75.1** | 256 |
| find miss (mlf 0.9) | 0.0 | 61.0 | **47.1** | 0.0 | 56.5 | 328 |
| iterate | 0.0 | **1.7** | 7.3 | 0.0 | 8.4 | 91.9 |

### small_string_max_12__uint64_t

| n=1,024 ns/op | absl::flat_hash_map | ankerl::unordered_dense_map | boost::unordered_flat_map | emhash::hash_map8 | sflat::flat_hash_map | std::unordered_map |
|---|---|---|---|---|---|---|
| insert (reserve) | 83.9 | 84.4 | **64.8** | 104 | 98.3 | 231 |
| insert (no reserve) | 206 | **169** | 171 | 293 | 225 | 281 |
| erase+insert | 141 | 118 | **79.9** | 168 | 382 | 125 |
| find hit | 53.0 | 51.9 | 51.4 | **42.2** | 54.0 | 45.8 |
| find miss | 31.1 | 31.4 | **29.3** | 34.2 | 39.8 | 84.3 |
| find 50% | 45.1 | 44.7 | 44.2 | **41.9** | 49.9 | 53.1 |
| find hit (mlf 0.9) | 53.8 | 52.1 | 50.9 | **44.8** | 52.2 | 75.6 |
| find miss (mlf 0.9) | 31.0 | 32.4 | **28.0** | 32.9 | 38.8 | 86.4 |
| iterate | 7.1 | 1.7 | 6.1 | **1.6** | 8.3 | 9.4 |

| n=100,000 ns/op | absl::flat_hash_map | ankerl::unordered_dense_map | boost::unordered_flat_map | emhash::hash_map8 | sflat::flat_hash_map | std::unordered_map |
|---|---|---|---|---|---|---|
| insert (reserve) | 103 | 88.6 | **79.9** | 204 | 136 | 334 |
| insert (no reserve) | 170 | 179 | **151** | 349 | 298 | 526 |
| erase+insert | 308 | **267** | 285 | 334 | 499 | 569 |
| find hit | **110** | 134 | 123 | 140 | 122 | 311 |
| find miss | 73.0 | 62.4 | **60.4** | 79.7 | 66.9 | 292 |
| find 50% | **102** | 120 | 113 | 125 | 112 | 363 |
| find hit (mlf 0.9) | **109** | 132 | 124 | 138 | 123 | 315 |
| find miss (mlf 0.9) | 74.0 | 62.9 | **60.3** | 78.3 | 66.8 | 291 |
| iterate | 11.5 | 1.7 | 5.8 | **1.6** | 8.4 | 45.0 |

| n=1,200,000 ns/op | absl::flat_hash_map | ankerl::unordered_dense_map | boost::unordered_flat_map | emhash::hash_map8 | sflat::flat_hash_map | std::unordered_map |
|---|---|---|---|---|---|---|
| insert (reserve) | 157 | 170 | **118** | 235 | 214 | 429 |
| insert (no reserve) | 240 | 261 | **189** | 537 | 329 | 714 |
| erase+insert | **291** | 394 | 293 | 429 | 558 | 727 |
| find hit | **148** | 197 | 157 | 194 | 152 | 429 |
| find miss | 87.6 | 98.2 | **77.9** | 117 | 80.0 | 398 |
| find 50% | 136 | 172 | 148 | 176 | **136** | 471 |
| find hit (mlf 0.9) | **147** | 196 | 158 | 192 | 149 | 427 |
| find miss (mlf 0.9) | 89.8 | 95.9 | 79.5 | 116 | **79.1** | 399 |
| iterate | 18.1 | 1.7 | 8.2 | **1.6** | 8.4 | 67.4 |

| n=10,000,000 ns/op | absl::flat_hash_map | ankerl::unordered_dense_map | boost::unordered_flat_map | emhash::hash_map8 | sflat::flat_hash_map | std::unordered_map |
|---|---|---|---|---|---|---|
| insert (reserve) | 219 | **195** | 202 | 280 | 229 | 484 |
| insert (no reserve) | 290 | 296 | **259** | 602 | 339 | 840 |
| erase+insert | **384** | 0.0 | 403 | 521 | 626 | 875 |
| find hit | 182 | 242 | 182 | 233 | **179** | 500 |
| find miss | 125 | 113 | **97.7** | 130 | 98.6 | 460 |
| find 50% | 188 | 236 | 177 | 206 | **165** | 552 |
| find hit (mlf 0.9) | 198 | 278 | 185 | 224 | **179** | 494 |
| find miss (mlf 0.9) | 135 | 113 | **97.8** | 127 | 97.9 | 458 |
| iterate | 17.6 | 1.7 | 7.6 | **1.7** | 8.4 | 84.8 |

### small_string_fix_12__uint64_t

| n=1,024 ns/op | absl::flat_hash_map | ankerl::unordered_dense_map | boost::unordered_flat_map | emhash::hash_map8 | sflat::flat_hash_map | std::unordered_map |
|---|---|---|---|---|---|---|
| insert (reserve) | 62.6 | 68.8 | **51.4** | 78.1 | 99.7 | 207 |
| insert (no reserve) | 153 | 143 | **136** | 218 | 199 | 258 |
| erase+insert | 113 | 110 | **72.4** | 122 | 305 | 192 |
| find hit | **41.3** | 49.9 | 46.6 | 48.6 | 54.5 | 96.5 |
| find miss | **26.2** | 32.9 | 31.3 | 35.8 | 41.5 | 98.9 |
| find 50% | 52.9 | 54.3 | 52.4 | **44.9** | 54.2 | 100 |
| find hit (mlf 0.9) | 49.3 | **48.7** | 50.1 | 49.9 | 55.1 | 96.8 |
| find miss (mlf 0.9) | 35.3 | 33.8 | **32.0** | 37.0 | 42.7 | 100 |
| iterate | 7.3 | **1.7** | 6.1 | 1.7 | 8.2 | 9.3 |

| n=100,000 ns/op | absl::flat_hash_map | ankerl::unordered_dense_map | boost::unordered_flat_map | emhash::hash_map8 | sflat::flat_hash_map | std::unordered_map |
|---|---|---|---|---|---|---|
| insert (reserve) | 89.8 | **48.9** | 61.4 | 181 | 158 | 305 |
| insert (no reserve) | 144 | 144 | **122** | 305 | 308 | 519 |
| erase+insert | 282 | **183** | 273 | 338 | 421 | 568 |
| find hit | 109 | **105** | 118 | 137 | 116 | 342 |
| find miss | 63.9 | 53.6 | **47.0** | 64.3 | 49.5 | 296 |
| find 50% | **103** | 115 | 106 | 120 | 103 | 344 |
| find hit (mlf 0.9) | **110** | 128 | 119 | 136 | 116 | 349 |
| find miss (mlf 0.9) | 64.1 | 53.2 | **47.1** | 65.3 | 51.2 | 293 |
| iterate | 11.4 | 1.7 | 4.6 | **0.8** | 7.7 | 46.4 |

| n=1,200,000 ns/op | absl::flat_hash_map | ankerl::unordered_dense_map | boost::unordered_flat_map | emhash::hash_map8 | sflat::flat_hash_map | std::unordered_map |
|---|---|---|---|---|---|---|
| insert (reserve) | 154 | 164 | **113** | 234 | 262 | 407 |
| insert (no reserve) | 205 | 243 | **176** | 506 | 359 | 691 |
| erase+insert | **294** | 393 | 301 | 423 | 499 | 726 |
| find hit | **146** | 196 | 155 | 193 | 148 | 484 |
| find miss | 84.5 | 97.9 | 74.8 | 108 | **71.2** | 423 |
| find 50% | **129** | 171 | 144 | 172 | 132 | 475 |
| find hit (mlf 0.9) | 146 | 195 | 155 | 191 | **145** | 480 |
| find miss (mlf 0.9) | 84.8 | 98.9 | 73.3 | 108 | **67.9** | 414 |
| iterate | 18.1 | **1.7** | 8.0 | 1.7 | 7.5 | 67.1 |

| n=10,000,000 ns/op | absl::flat_hash_map | ankerl::unordered_dense_map | boost::unordered_flat_map | emhash::hash_map8 | sflat::flat_hash_map | std::unordered_map |
|---|---|---|---|---|---|---|
| insert (reserve) | 216 | 195 | **186** | 284 | 257 | 460 |
| insert (no reserve) | 265 | 283 | **236** | 581 | 357 | 813 |
| erase+insert | **379** | 0.0 | 409 | 517 | 567 | 868 |
| find hit | 184 | 238 | 182 | 225 | **178** | 559 |
| find miss | 126 | 114 | 97.4 | 122 | **96.9** | 486 |
| find 50% | 174 | 229 | 175 | 200 | **162** | 552 |
| find hit (mlf 0.9) | 199 | 274 | 181 | 225 | **177** | 561 |
| find miss (mlf 0.9) | 131 | 114 | 98.4 | 120 | **97.2** | 486 |
| iterate | 16.3 | **1.6** | 7.7 | 1.7 | 8.0 | 85.1 |

### mid_string_max_24__uint64_t

| n=1,024 ns/op | absl::flat_hash_map | ankerl::unordered_dense_map | boost::unordered_flat_map | emhash::hash_map8 | sflat::flat_hash_map | std::unordered_map |
|---|---|---|---|---|---|---|
| insert (reserve) | 125 | 114 | **61.1** | 149 | 154 | 254 |
| insert (no reserve) | 255 | **211** | 225 | 345 | 330 | 323 |
| erase+insert | 184 | 188 | **137** | 228 | 508 | 275 |
| find hit | 70.1 | 67.6 | 70.8 | **64.5** | 73.1 | 108 |
| find miss | 36.9 | 37.3 | **34.8** | 37.5 | 44.9 | 97.7 |
| find 50% | 56.0 | 56.5 | 54.2 | **53.6** | 64.4 | 102 |
| find hit (mlf 0.9) | 68.9 | 69.7 | 69.2 | **62.6** | 69.5 | 107 |
| find miss (mlf 0.9) | 35.8 | 36.7 | **33.9** | 37.7 | 44.6 | 97.2 |
| iterate | 7.4 | 1.6 | 6.6 | **1.6** | 8.0 | 9.0 |

| n=100,000 ns/op | absl::flat_hash_map | ankerl::unordered_dense_map | boost::unordered_flat_map | emhash::hash_map8 | sflat::flat_hash_map | std::unordered_map |
|---|---|---|---|---|---|---|
| insert (reserve) | 142 | 137 | **127** | 257 | 186 | 396 |
| insert (no reserve) | 232 | 228 | **207** | 409 | 404 | 607 |
| erase+insert | 433 | **414** | 429 | 510 | 762 | 677 |
| find hit | **189** | 208 | 198 | 209 | 196 | 381 |
| find miss | 107 | 101 | **91.9** | 107 | 103 | 334 |
| find 50% | 167 | 173 | 174 | 172 | **166** | 399 |
| find hit (mlf 0.9) | **190** | 207 | 202 | 207 | 193 | 382 |
| find miss (mlf 0.9) | 106 | 98.6 | **92.9** | 107 | 102 | 328 |
| iterate | 11.1 | 1.6 | 4.6 | **1.5** | 8.4 | 45.2 |

| n=1,200,000 ns/op | absl::flat_hash_map | ankerl::unordered_dense_map | boost::unordered_flat_map | emhash::hash_map8 | sflat::flat_hash_map | std::unordered_map |
|---|---|---|---|---|---|---|
| insert (reserve) | 211 | 201 | **184** | 291 | 261 | 493 |
| insert (no reserve) | 347 | 323 | **318** | 632 | 476 | 778 |
| erase+insert | 403 | 490 | **379** | 549 | 814 | 736 |
| find hit | 239 | 288 | 247 | 274 | **231** | 477 |
| find miss | 133 | 137 | **115** | 146 | 121 | 456 |
| find 50% | 208 | 238 | 211 | 230 | **202** | 521 |
| find hit (mlf 0.9) | 233 | 285 | 245 | 273 | **232** | 478 |
| find miss (mlf 0.9) | 130 | 117 | **115** | 143 | 119 | 460 |
| iterate | 18.2 | 1.7 | 8.1 | **1.5** | 8.0 | 77.2 |

| n=10,000,000 ns/op | absl::flat_hash_map | ankerl::unordered_dense_map | boost::unordered_flat_map | emhash::hash_map8 | sflat::flat_hash_map | std::unordered_map |
|---|---|---|---|---|---|---|
| insert (reserve) | 265 | **239** | 264 | 354 | 291 | 549 |
| insert (no reserve) | 419 | **366** | 404 | 723 | 523 | 891 |
| erase+insert | **509** | 0.0 | 527 | 719 | 964 | 976 |
| find hit | 313 | 381 | 320 | 382 | **280** | 578 |
| find miss | 186 | 164 | **143** | 173 | 156 | 531 |
| find 50% | 268 | 307 | 264 | 293 | **246** | 670 |
| find hit (mlf 0.9) | 303 | 369 | 300 | 350 | **283** | 620 |
| find miss (mlf 0.9) | 175 | 153 | **144** | 166 | 148 | 569 |
| iterate | 16.2 | 1.7 | 7.6 | **1.6** | 7.9 | 97.1 |

### mid_string_fix_24__uint64_t

| n=1,024 ns/op | absl::flat_hash_map | ankerl::unordered_dense_map | boost::unordered_flat_map | emhash::hash_map8 | sflat::flat_hash_map | std::unordered_map |
|---|---|---|---|---|---|---|
| insert (reserve) | 124 | 119 | **112** | 137 | 186 | 257 |
| insert (no reserve) | 218 | **181** | 199 | 293 | 310 | 306 |
| erase+insert | 241 | 245 | **208** | 252 | 532 | 374 |
| find hit | 114 | 108 | 112 | **106** | 116 | 189 |
| find miss | 54.8 | 54.3 | **49.8** | 50.6 | 63.7 | 153 |
| find 50% | 96.5 | 91.4 | 89.8 | **80.3** | 98.5 | 180 |
| find hit (mlf 0.9) | 113 | 110 | 111 | **106** | 114 | 186 |
| find miss (mlf 0.9) | 53.7 | 54.5 | 49.9 | **48.7** | 64.2 | 156 |
| iterate | 6.9 | 1.7 | 6.8 | **1.7** | 7.2 | 26.3 |

| n=100,000 ns/op | absl::flat_hash_map | ankerl::unordered_dense_map | boost::unordered_flat_map | emhash::hash_map8 | sflat::flat_hash_map | std::unordered_map |
|---|---|---|---|---|---|---|
| insert (reserve) | 198 | 168 | **165** | 315 | 259 | 436 |
| insert (no reserve) | 282 | **223** | 262 | 441 | 548 | 658 |
| erase+insert | 576 | **497** | 665 | 593 | 941 | 731 |
| find hit | **251** | 279 | 278 | 284 | 256 | 417 |
| find miss | 140 | 137 | 124 | **113** | 145 | 344 |
| find 50% | 225 | 224 | 233 | **208** | 222 | 436 |
| find hit (mlf 0.9) | **253** | 279 | 279 | 285 | 255 | 417 |
| find miss (mlf 0.9) | 141 | 138 | 120 | **113** | 144 | 346 |
| iterate | 11.5 | 1.7 | 5.5 | **1.7** | 8.0 | 47.1 |

| n=1,200,000 ns/op | absl::flat_hash_map | ankerl::unordered_dense_map | boost::unordered_flat_map | emhash::hash_map8 | sflat::flat_hash_map | std::unordered_map |
|---|---|---|---|---|---|---|
| insert (reserve) | 285 | **253** | 261 | 354 | 333 | 510 |
| insert (no reserve) | 443 | **319** | 522 | 643 | 719 | 808 |
| erase+insert | 476 | 560 | **455** | 630 | 1043 | 841 |
| find hit | 323 | 355 | **310** | 345 | 348 | 472 |
| find miss | 177 | 181 | **136** | 146 | 185 | 481 |
| find 50% | 268 | 281 | 265 | **261** | 263 | 573 |
| find hit (mlf 0.9) | **292** | 350 | 313 | 341 | 309 | 493 |
| find miss (mlf 0.9) | 175 | 174 | **136** | 145 | 169 | 480 |
| iterate | 18.5 | **1.6** | 7.8 | 1.7 | 8.3 | 82.4 |

| n=10,000,000 ns/op | absl::flat_hash_map | ankerl::unordered_dense_map | boost::unordered_flat_map | emhash::hash_map8 | sflat::flat_hash_map | std::unordered_map |
|---|---|---|---|---|---|---|
| insert (reserve) | 344 | **280** | 355 | 422 | 388 | 584 |
| insert (no reserve) | 651 | **377** | 645 | 777 | 772 | 960 |
| erase+insert | **638** | 0.0 | 646 | 832 | 1271 | 1121 |
| find hit | **449** | 564 | 474 | 547 | 466 | 670 |
| find miss | 268 | 237 | 195 | **184** | 240 | 647 |
| find 50% | 372 | 404 | 373 | 398 | **367** | 758 |
| find hit (mlf 0.9) | **423** | 513 | 478 | 550 | 462 | 626 |
| find miss (mlf 0.9) | 244 | 208 | **166** | 168 | 216 | 633 |
| iterate | 17.3 | **1.6** | 7.6 | 1.6 | 7.7 | 105 |

### long_string_max_64__uint64_t

| n=1,024 ns/op | absl::flat_hash_map | ankerl::unordered_dense_map | boost::unordered_flat_map | emhash::hash_map8 | sflat::flat_hash_map | std::unordered_map |
|---|---|---|---|---|---|---|
| insert (reserve) | 158 | 160 | **144** | 171 | 220 | 280 |
| insert (no reserve) | 288 | **253** | 273 | 396 | 446 | 362 |
| erase+insert | 266 | 255 | **205** | 293 | 652 | 377 |
| find hit | 116 | 114 | 114 | **110** | 116 | 211 |
| find miss | 58.7 | 57.5 | 56.0 | **54.9** | 67.4 | 172 |
| find 50% | 90.7 | 92.7 | 91.2 | **89.9** | 100 | 195 |
| find hit (mlf 0.9) | 116 | 114 | 116 | **110** | 118 | 210 |
| find miss (mlf 0.9) | 60.5 | 56.8 | 55.6 | **54.0** | 65.2 | 172 |
| iterate | 7.0 | **1.7** | 6.7 | 1.7 | 8.2 | 27.1 |

| n=100,000 ns/op | absl::flat_hash_map | ankerl::unordered_dense_map | boost::unordered_flat_map | emhash::hash_map8 | sflat::flat_hash_map | std::unordered_map |
|---|---|---|---|---|---|---|
| insert (reserve) | 182 | 184 | **158** | 327 | 246 | 449 |
| insert (no reserve) | 309 | **266** | 288 | 516 | 541 | 680 |
| erase+insert | 584 | **511** | 588 | 636 | 1069 | 798 |
| find hit | **265** | 303 | 280 | 338 | 269 | 518 |
| find miss | 149 | 147 | **142** | 151 | 153 | 456 |
| find 50% | **230** | 247 | 241 | 248 | 232 | 543 |
| find hit (mlf 0.9) | **264** | 306 | 280 | 315 | 270 | 540 |
| find miss (mlf 0.9) | 152 | 147 | **142** | 153 | 146 | 453 |
| iterate | 11.1 | 1.6 | 5.6 | **1.1** | 8.4 | 105 |

| n=1,200,000 ns/op | absl::flat_hash_map | ankerl::unordered_dense_map | boost::unordered_flat_map | emhash::hash_map8 | sflat::flat_hash_map | std::unordered_map |
|---|---|---|---|---|---|---|
| insert (reserve) | 331 | 260 | **242** | 435 | 311 | 536 |
| insert (no reserve) | 584 | **401** | 518 | 807 | 678 | 764 |
| erase+insert | 516 | 0.0 | **473** | 684 | 1125 | 884 |
| find hit | 332 | 379 | 345 | 374 | **323** | 552 |
| find miss | 188 | 180 | **164** | 190 | 172 | 525 |
| find 50% | 282 | 321 | 290 | 303 | **275** | 602 |
| find hit (mlf 0.9) | 328 | 399 | 344 | 372 | **323** | 549 |
| find miss (mlf 0.9) | 183 | 182 | **160** | 185 | 171 | 523 |
| iterate | 18.7 | **1.6** | 7.2 | 1.7 | 8.1 | 92.9 |

| n=10,000,000 ns/op | absl::flat_hash_map | ankerl::unordered_dense_map | boost::unordered_flat_map | emhash::hash_map8 | sflat::flat_hash_map | std::unordered_map |
|---|---|---|---|---|---|---|
| insert (reserve) | 386 | 377 | 357 | 492 | **337** | 633 |
| insert (no reserve) | 710 | **570** | 643 | 920 | 723 | 985 |
| erase+insert | **632** | 0.0 | 644 | 911 | 1435 | 1187 |
| find hit | 459 | 562 | 478 | 590 | **425** | 746 |
| find miss | 278 | 248 | **214** | 238 | 233 | 671 |
| find 50% | 385 | 427 | 424 | 424 | **357** | 748 |
| find hit (mlf 0.9) | **452** | 537 | 523 | 541 | 454 | 712 |
| find miss (mlf 0.9) | 249 | 218 | **195** | 223 | 209 | 662 |
| iterate | 17.4 | 1.7 | 7.7 | **1.6** | 8.1 | 115 |

### long_string_fix_64__uint64_t

| n=1,024 ns/op | absl::flat_hash_map | ankerl::unordered_dense_map | boost::unordered_flat_map | emhash::hash_map8 | sflat::flat_hash_map | std::unordered_map |
|---|---|---|---|---|---|---|
| insert (reserve) | 139 | 146 | **134** | 165 | 210 | 288 |
| insert (no reserve) | 270 | **237** | 260 | 364 | 442 | 325 |
| erase+insert | 305 | 285 | **216** | 317 | 746 | 361 |
| find hit | 157 | **147** | 152 | 157 | 157 | 271 |
| find miss | 89.6 | 82.5 | **79.7** | 84.6 | 95.6 | 213 |
| find 50% | 134 | 136 | 134 | **123** | 146 | 248 |
| find hit (mlf 0.9) | 152 | **149** | 151 | 153 | 156 | 267 |
| find miss (mlf 0.9) | 87.6 | 82.7 | **79.3** | 83.2 | 100 | 212 |
| iterate | 6.8 | 1.7 | 6.8 | **1.6** | 8.1 | 26.9 |

| n=100,000 ns/op | absl::flat_hash_map | ankerl::unordered_dense_map | boost::unordered_flat_map | emhash::hash_map8 | sflat::flat_hash_map | std::unordered_map |
|---|---|---|---|---|---|---|
| insert (reserve) | 232 | 217 | **180** | 394 | 283 | 477 |
| insert (no reserve) | 365 | **281** | 351 | 592 | 624 | 742 |
| erase+insert | 651 | **539** | 605 | 684 | 1327 | 798 |
| find hit | **316** | 388 | 333 | 393 | 338 | 650 |
| find miss | 203 | 192 | 185 | **180** | 201 | 521 |
| find 50% | 294 | 307 | **289** | 313 | 292 | 615 |
| find hit (mlf 0.9) | 330 | 385 | 331 | 395 | **330** | 651 |
| find miss (mlf 0.9) | 208 | 191 | 187 | **186** | 205 | 523 |
| iterate | 11.4 | 1.7 | 5.6 | **1.6** | 8.4 | 113 |

| n=1,200,000 ns/op | absl::flat_hash_map | ankerl::unordered_dense_map | boost::unordered_flat_map | emhash::hash_map8 | sflat::flat_hash_map | std::unordered_map |
|---|---|---|---|---|---|---|
| insert (reserve) | 316 | **288** | 298 | 406 | 367 | 572 |
| insert (no reserve) | 597 | **380** | 565 | 819 | 792 | 869 |
| erase+insert | 537 | 605 | **518** | 724 | 1372 | 942 |
| find hit | **395** | 492 | 417 | 483 | 427 | 614 |
| find miss | 237 | 226 | **211** | 221 | 231 | 575 |
| find 50% | 346 | 375 | 357 | 364 | **339** | 644 |
| find hit (mlf 0.9) | 410 | 493 | 422 | 478 | **408** | 611 |
| find miss (mlf 0.9) | 228 | 217 | **205** | 216 | 219 | 568 |
| iterate | 18.3 | **1.6** | 8.0 | 1.7 | 7.9 | 88.6 |

| n=10,000,000 ns/op | absl::flat_hash_map | ankerl::unordered_dense_map | boost::unordered_flat_map | emhash::hash_map8 | sflat::flat_hash_map | std::unordered_map |
|---|---|---|---|---|---|---|
| insert (reserve) | 372 | **333** | 405 | 483 | 384 | 636 |
| insert (no reserve) | 784 | **469** | 802 | 981 | 867 | 1041 |
| erase+insert | 683 | 0.0 | **650** | 946 | 1744 | 1256 |
| find hit | **537** | 722 | 597 | 670 | 607 | 792 |
| find miss | 339 | 308 | **278** | 286 | 299 | 706 |
| find 50% | **458** | 519 | 493 | 500 | 508 | 809 |
| find hit (mlf 0.9) | **543** | 683 | 628 | 662 | 652 | 784 |
| find miss (mlf 0.9) | 313 | 281 | **261** | 266 | 310 | 701 |
| iterate | 17.7 | **1.6** | 7.1 | 1.7 | 8.4 | 114 |

