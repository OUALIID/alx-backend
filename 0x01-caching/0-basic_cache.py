#!/usr/bin/env python
"""
0x01. Caching
"""
from base_caching import BaseCaching


class BasicCache(BaseCaching):
    """ BasicCache class. """
    def put(self, key, item):
        """ Add an item in the cache """
        if key and item is not None:
            self.cache_data[key] = item

    def get(self, key):
        """ Get an item by key"""
        if key in self.cache_data:
            return self.cache_data[key]
        return None
