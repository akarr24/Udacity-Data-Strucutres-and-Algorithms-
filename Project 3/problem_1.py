# -*- coding: utf-8 -*-

def sqrt(number):
    """
    Calculate the floored square root of a number

    Args:
       number(int): Number to find the floored squared root
    Returns:
       int: Floored Square Root
    """
    if number == 0 or number == 1:
        return number
    
    # Perform a Binary search for square root
    s = 0
    e = number / 2
    
    while s <= e:
        mid = (s + e) // 2
        
        if mid*mid == number:
            return mid
        
        if mid*mid < number:
            s = mid + 1
        
        else:
            e = mid - 1
       
    return mid
    
            
        
    

print ("Pass" if  (3 == sqrt(9)) else "Fail")
# 3
print ("Pass" if  (0 == sqrt(0)) else "Fail")
# 0
print ("Pass" if  (4 == sqrt(16)) else "Fail")
# 4
print ("Pass" if  (1 == sqrt(1)) else "Fail")
# 1
print ("Pass" if  (5 == sqrt(27)) else "Fail")
# 5
print ("Pass" if  (6 == sqrt(36)) else "Fail")
#6
print ("Pass" if  (6 == sqrt(42)) else "Fail")
# 6
print ("Pass" if  (7 == sqrt(49)) else "Fail")
# 7
print ("Pass" if  (91 == sqrt(8281)) else "Fail")
#91