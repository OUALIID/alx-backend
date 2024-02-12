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
        self.lfu_cache = []

    def put(self, key, item):
        """ Add an item to the cache. """
        if key is not None and item is not None:
            if key in self.cache_data:
                self.lfu_cache.remove(key)
            elif len(self.cache_data) >= BaseCaching.MAX_ITEMS:
                lru_key = self.lfu_cache.pop(0)
                del self.cache_data[lru_key]
                print("DISCARD:", lru_key)
            self.cache_data[key] = item
            self.lfu_cache.append(key)
        else:
            return None

    def get(self, key):
        """ Retrieve an item from the cache. """
        if key in self.cache_data:
            return self.cache_data[key]
        return None