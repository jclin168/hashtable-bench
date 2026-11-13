#pragma once

#include "Hash.h"
#include "Allocator.h"
#include "emhash-map/include/emhash/hash_table8.hpp"

static const char* MAP_NAME = "emhash::hash_map8";

template <class Key, class T>
using Map = emhash8::HashMap<Key, T, Hash<Key>, std::equal_to<>,
        Allocator<std::pair<Key, T>>>;
