# -*- coding: utf-8 -*-
def get_min_max(ints):
    """
    Return a tuple(min, max) out of list of unsorted integers.

    Args:
       ints(list): list of integers containing one or more integers
    """
    assert(len(ints) > 0)
    min = ints[0]
    max = ints[0]
   
    for i in range(0, len(ints)):
       num = ints[i]
       if num < min:
           min  = num
       if num > max:
           max = num
    print(min, max)
    return min, max

## Example Test Case of Ten Integers
import random

l = [i for i in range(0, 10)]  # a list containing 0 - 9
random.shuffle(l)
print ("Pass" if ((0, 9) == get_min_max(l)) else "Fail")
# 0 9

l = [i for i in range(0, 11)]  # a list containing 0 - 9
random.shuffle(l)
print ("Pass" if ((0, 10) == get_min_max(l)) else "Fail")
# 0 10

l = [i for i in range(1, 1001)]  # a list containing 0 - 9
random.shuffle(l)
print ("Pass" if ((1, 1000) == get_min_max(l)) else "Fail")
# 1 1000

print(get_min_max([0]))
# 0 0

print(get_min_max([0,0]))
# 0 0