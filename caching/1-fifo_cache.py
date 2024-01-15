#!/usr/bin/env python3
"""fifo caching"""
from base_caching import BaseCaching


class FIFOCache(BaseCaching):
    """inherits from base_caching"""
    def __init__(self):
        super().__init__()
        self.key_indexes = []

    def put(self, key, item):
        """assign to the dict"""
        if key and item:
            if key in self.cache_data:
                self.cache_data[key] = item
                return
            if len(self.cache_data) >= BaseCaching.MAX_ITEMS:
                item_to_be_discarded = self.key_indexes.pop(0)
                del self.cache_data[item_to_be_discarded]
                print(f"DISCARD:, {item_to_be_discarded}\n")
            self.cache_data[key] = item
            self.key_indexes.append(key)

    def get(self, key):
        """returns the value in dict"""
        if key in self.cache_data:
            return self.cache_data[key]
        return None
