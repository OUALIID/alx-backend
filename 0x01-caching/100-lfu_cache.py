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
                self.cache_data[key] = item
                self.lfu_cache[key] += 1
            else:
                if len(self.cache_data) >= BaseCaching.MAX_ITEMS:
                    least_used_key = min(
                        self.lfu_cache,
                        key=self.lfu_cache.get
                    )
                    print("DISCARD:", least_used_key)
                    del self.cache_data[least_used_key]
                    del self.lfu_cache[least_used_key]
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
