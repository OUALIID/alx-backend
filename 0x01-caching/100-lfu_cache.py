#!/usr/bin/env python
"""
Module for implementing a LFUCache.
"""
from base_caching import BaseCaching


class LFUCache(BaseCaching):
    """ Class representing a LFUCache."""
    def __init__(self):
        """ Initialize a new LFUCache. """
        super().__init__()
        self.lfu_cache = {}

    def put(self, key, item):
        """
        Add an item to the cache, and remove the least used item.
        """
        if key and item is not None:
            if key in self.cache_data:
                self.lfu_cache[key] += 1
                self.cache_data[key] = item
                return

            elif len(self.cache_data) >= BaseCaching.MAX_ITEMS:
                least = None
                least_count = float('inf')
                for k, v in self.lfu_cache.items():
                    if v < least_count:
                        least = k
                        least_count = v
                print("DISCARD:", least)
                del self.cache_data[least]
                del self.lfu_cache[least]

            self.lfu_cache[key] = 0
            self.cache_data[key] = item
        else:
            return

    def get(self, key):
        """ Retrieve an item from the cache. """
        if key in self.cache_data:
            self.lfu_cache[key] += 1
            return self.cache_data[key]
        return None
