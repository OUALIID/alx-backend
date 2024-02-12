#!/usr/bin/env python
"""
Module for implementing a FIFO cache.
"""
from base_caching import BaseCaching


class FIFOCache(BaseCaching):
    """ A class representing a FIFO cache."""
    def __init__(self):
        """
        Initialize a new FIFO cache.
        """
        super().__init__()
        self.cache_order = []

    def put(self, key, item):
        """ Add an item to the cache."""
        if key and item is not None:
            if len(self.cache_data) >= BaseCaching.MAX_ITEMS:
                oldest_key = self.cache_order.pop(0)
                del self.cache_data[oldest_key]
                print("DISCARD:", oldest_key)
            self.cache_data[key] = item
            self.cache_order.append(key)

    def get(self, key):
        """ Retrieve an item from the cache. """
        if key in self.cache_data:
            return self.cache_data[key]
        return None
