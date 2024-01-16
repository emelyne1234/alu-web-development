#!/usr/bin/env python3
"""lifo caching"""
from base_caching import BaseCaching


class LIFOCache(BaseCaching):
    """inherits from base_caching"""
    def __init__(self):
        super().__init__()
        self.key_indexes = []


    def put(self, key, item):
        """assigned to the dict"""
        if key and item:
            if len(self.cache_data) >= self.MAX_ITEMS:
                if key in self.cache_data:
                    del self.cache_data[key]
                    self.key_indexes.remove(key)
                else:
                    del self.cache_data[self.key_indexes[self.MAX_ITEMS - 1]]
                    item_to_be_discarded = self.key_indexes.pop(self.MAX_ITEMS - 1)
                    print("DISCARD:", item_to_be_discarded)
            self.cache_data[key] = item
            self.key_indexes.append(key)

    def get(self, key):
        ''' returns the value '''
        if key in self.cache_data:
            return self.cache_data[key]
        return None
