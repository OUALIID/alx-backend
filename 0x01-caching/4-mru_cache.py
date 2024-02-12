#!/usr/bin/env python
"""
Module for implementing a MRUCache.
"""
from base_caching import BaseCaching


class MRUCache(BaseCaching):
    """ Class representing a MRUCache."""
    def __init__(self):
        """ Initialize a new MRUCache. """
        super().__init__()
        self.mru_cache = []

    def put(self, key, item):
        """ Add an item to the cache. """
        if key is not None and item is not None:
            if key in self.cache_data:
                self.mru_cache.remove(key)
            elif len(self.cache_data) >= BaseCaching.MAX_ITEMS:
                lru_key = self.mru_cache.pop()
                del self.cache_data[lru_key]
                print("DISCARD:", lru_key)
            self.cache_data[key] = item
            self.mru_cache.append(key)
        else:
            return None

    def get(self, key):
        """ Retrieve an item from the cache. """
        if key in self.cache_data:
            # self.mru_cache.remove(key)
            self.mru_cache.append(key)
            return self.cache_data[key]
        return None
