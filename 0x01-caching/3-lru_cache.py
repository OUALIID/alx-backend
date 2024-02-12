#!/usr/bin/env python
"""
Module for implementing a LRUCache.
"""
from base_caching import BaseCaching

class LRUCache(BaseCaching):
    """ Class representing a LRUCache."""
    def __init__(self):
        """ Initialize a new LRUCache. """
        super().__init__()
        self.cache_order = []

    def put(self, key, item):
        """ Add an item to the cache. """
        if key is not None and item is not None:
            if key in self.cache_data:
                self.cache_order.remove(key)
            elif len(self.cache_data) >= BaseCaching.MAX_ITEMS:
                lru_key = self.cache_order.pop(0)
                del self.cache_data[lru_key]
                print("DISCARD:", lru_key)
            self.cache_data[key] = item
            self.cache_order.append(key)

    def get(self, key):
        """ Retrieve an item from the cache. """
        if key in self.cache_data:
            return self.cache_data[key]
        return None
