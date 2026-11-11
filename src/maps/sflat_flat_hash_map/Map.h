#pragma once

#include "Hash.h"
#include "Allocator.h"
#include "sflat_hash_map/include/sflat/flat_hash_map.hpp"

static const char* MAP_NAME = "sflat::flat_hash_map";

template <class Key, class T>
using Map = sflat::flat_hash_map<Key, T, Hash<Key>, std::equal_to<>,
        Allocator<std::pair<const Key, T>>>;
