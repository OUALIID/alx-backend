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
        self.key_usage_count = {}

    def put(self, key, item):
        """ Add an item to the cache. """
        if key is not None and item is not None:
            self.key_usage_count[key] = self.key_usage_count.get(key, 0) + 1
            if len(self.cache_data) >= BaseCaching.MAX_ITEMS:
                lfu_key = min(self.key_usage_count, key=self.key_usage_count.get)
                if lfu_key in self.cache_data:
                    del self.cache_data[lfu_key]
                    del self.key_usage_count[lfu_key]
                    print("DISCARD:", lfu_key)
            self.cache_data[key] = item

    def get(self, key):
        """ Retrieve an item from the cache. """
        if key in self.cache_data:
            self.key_usage_count[key] += 1
            return self.cache_data[key]
        return None
