# -*- coding: utf-8 -*-
def rearrange_digits(input_list):
    """
    Rearrange Array Elements so as to form two number such that their sum is maximum.

    Args:
       input_list(list): Input List
    Returns:
       (int),(int): Two maximum sums
    """
    quicksort(input_list, 0, len(input_list) - 1)
    
    x = 0
    y = 0
    i = 0
    factor = 1
    
    while i < len(input_list):
        x += input_list[i] * factor
        if i + 1 < len(input_list):
            y += input_list[i + 1] * factor
        factor *= 10
        i += 2
    
    return x,y

def quicksort(array, low, high):
    if low >= high:
        return array
    
    pivot_position = low
    current = low
    pivot = array[high]
    
    while current < high :
        if array[current] < pivot:
            temp = array[current]
            array[current] = array[pivot_position]
            array[pivot_position] = temp
            pivot_position += 1
            current += 1
        else:
            current += 1

    array[high]  = array[pivot_position]
    array[pivot_position] = pivot

    quicksort(array, low, pivot_position - 1)
    quicksort(array, pivot_position + 1, high)

    return array

def test_function(test_case):
    
    output = rearrange_digits(test_case[0])
    print(output)
    solution = test_case[1]
    if sum(output) == sum(solution):
        print("Pass")
    else:
        print("Fail")

test_function([[1, 2, 3, 4, 5], [542, 31]])
# 542, 31
test_case = [[4, 6, 2, 5, 9, 8], [964, 852]]
test_function(test_case)
# 964, 852
test_function([[], [0, 0]])
# 0, 0
test_function([[1,1], [1,1]])
#1 ,1 

import random
l = [i for i in range(0, 11)]
random.shuffle(l)

test_function([l, [1086420, 97531]])
# 1086420, 97531


