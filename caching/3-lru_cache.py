#!/usr/bin/python3
''' lru caching '''

from collections import OrderedDict

BaseCaching = __import__('base_caching').BaseCaching


class LRUCache(BaseCaching):
    ''' inherits from base_caching '''

    def __init__(self):
        super().__init__()
        self.lru_order = OrderedDict()

    def put(self, key, item):
        ''' gets the item '''
        if key and item:
            self.lru_order[key] = item
            self.lru_order.move_to_end(key)
            self.cache_data[key] = item

        if len(self.cache_data) > BaseCaching.MAX_ITEMS:
            item_to_be_discarded = next(iter(self.lru_order))
            del self.cache_data[item_to_be_discarded]
            print("DISCARD:", item_to_be_discarded)

        if len(self.lru_order) > BaseCaching.MAX_ITEMS:
            self.lru_order.popitem(last=False)

    def get(self, key):
        ''' returns the key value '''
        if key in self.cache_data:
            self.lru_order.move_to_end(key)
            return self.cache_data[key]
        return None
