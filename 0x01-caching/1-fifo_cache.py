#!/usr/bin/python3
"""1-fifo_cache"""

BaseCaching = __import__('base_caching').BaseCaching


class FIFOCache(BaseCaching):
    def __init__(self):
        super().__init__()

    def put(self, key, item):
        if key is not None and item is not None:
            if len(self.cache_data) >= self.MAX_ITEMS:
                first_item = next(iter(self.cache_data))
                self.cache_data.pop(first_item)
                print("DISCARD: {}".format(first_item))
            self.cache_data[key] = item

    def get(self, key):
        if key is None or key not in self.cache_data:
            return None
        return self.cache_data[key]
