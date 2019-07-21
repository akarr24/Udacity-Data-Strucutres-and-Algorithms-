# -*- coding: utf-8 -*-
from collections import OrderedDict
class LRU_Cache(object):

    def __init__(self, capacity):
        # Initialize class variables
        self.capacity = capacity
        self.cache = OrderedDict()
        assert capacity > 0, 'Size should be greater than 0'
        

    def get(self, key):
        # Retrieve item from provided key. Return -1 if nonexistent. 
        if key not in self.cache:
            return -1
        value = self.cache.pop(key) # extracts the value from the cache
        self.cache[key] = value #update the cache and put the value on the right (recently used)
        return value

    def set(self, key, value):
        # Set the value if the key is not present in the cache. If the cache is at capacity remove the oldest item. 
        if key in self.cache: #Only operation that takes O(n) time
            self.cache.pop(key) #if key is present, removes the key and value
        elif len(self.cache) == self.capacity: #if cache is full
            self.cache.popitem(last = False) #removes the leftmost (least recently used) item
        self.cache[key] = value #updates the cache
    
    def __str__(self):
        
        # print cache by usage order (oldest first)
        string = '{ '
        for key in self.cache:
            string += str(key) + ':' + str(self.cache[key]) + ', '
        string += ' }'
        return string
        

#Test Cases
our_cache = LRU_Cache(5)

our_cache.set(1, 1)
our_cache.set(2, 2)
our_cache.set(3, 3)
print(our_cache)
# fill partially
# { 1:1, 2:2, 3:3 }

our_cache.set(4, 4)
our_cache.set(5, 5)
print(our_cache)
# fill completely
# { 1:1, 2:2, 3:3, 4:4, 5:5 }

our_cache.get(1)
our_cache.get(2)
our_cache.get(3)
print(our_cache)
# 'use' old values
# { 4:4, 5:5, 1:1, 2:2, 3:3 }

our_cache.set(6, 6)
our_cache.set(7, 7)
our_cache.set(8, 8)
print(our_cache)
# overflow cache
# { 2:2, 3:3, 6:6, 7:7, 8:8 }

our_cache.set(9, 9)
our_cache.set(9, 10)
print(our_cache)
# change value
# { 3:3, 6:6, 7:7, 8:8, 9:10 }

#Zero Capacity/Empty Cache
our_cache = LRU_Cache(0)
our_cache.set(1,1)
our_cache.get(1)
print(our_cache)
#Assertion Error: Size should be greater than 0