#!/usr/bin/env python3
"""base caching module"""
from base_caching import BaseCaching


class BasicCache(BaseCaching):
    """inherits from base_caching"""
    def put(self, key, item):
        """assign to the dict"""
        if key and item:
            self.cache_data[key] = item

    def get(self, key):
        """returns value in dict linked to key"""
        if key is None or self.cache_data.get(key) is None:
            return None
        return self.cache_data.get(key)
    