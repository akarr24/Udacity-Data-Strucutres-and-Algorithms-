# -*- coding: utf-8 -*-
def rotated_array_search(input_list, number):
    """
    Find the index by searching in a rotated sorted array

    Args:
       input_list(array), number(int): Input array to search and the target
    Returns:
       int: Index or -1
    """
    low = 0
    high = len(input_list) - 1
   
    return search(input_list, low, high, number)

def search(input_list, low, high, number):
    if low > high:
        return -1
    
    mid = (low + high) // 2
    if input_list[mid] == number:
        return mid
    
    # if array[l...mid is sorted]
    if input_list[low] < input_list[mid]:
        
        if number >= input_list[low] and number <= input_list[mid]:
            return search(input_list, low, mid - 1, number)
        return search(input_list, mid+1, high, number)
    
    #if array[low....mid] is not sorted
    if number >= input_list[mid] and number <= input_list[high]:
        return search(input_list, mid+1, high, number)
    return search(input_list, low, mid-1, number)

def linear_search(input_list, number):
    for index, element in enumerate(input_list):
        if element == number:
            return index
    return -1

def test_function(test_case):
    input_list = test_case[0]
    number = test_case[1]
    if linear_search(input_list, number) == rotated_array_search(input_list, number):
        print("Pass")
    else:
        print("Fail")

test_function([[6, 7, 8, 9, 10, 1, 2, 3, 4], 6])
# 0
test_function([[6, 7, 8, 9, 10, 1, 2, 3, 4], 1])
# 5
test_function([[6, 7, 8, 1, 2, 3, 4], 8])
# 2
test_function([[6, 7, 8, 1, 2, 3, 4], 1])
# 3
test_function([[6, 7, 8, 1, 2, 3, 4], 10])
# -1
test_function([[], 0])
# -1
test_function([[0], 0])
# 0