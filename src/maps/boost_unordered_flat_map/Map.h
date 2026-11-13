#pragma once

#include "Hash.h"
#include "Allocator.h"
#include <boost/unordered/unordered_flat_map.hpp>

static const char* MAP_NAME = "boost::unordered_flat_map";

template <class Key, class T>
using Map = boost::unordered_flat_map<Key, T, Hash<Key>, std::equal_to<>,
        Allocator<std::pair<const Key, T>>>;
