# -*- coding: utf-8 -*-
"""
Created on Sat May  4 23:49:21 2019

@author: adikar
"""

dict1 = {'a': 12, 'for': 25, 'c': 9} 
dict2 = {'Geeks': 100, 'geek': 200, 'for': 300} 

dict3 = dict()
# adding the values with common key 
for key in dict2: 
	if key in dict1: 
		 dict2[key] = dict2[key] + dict1[key] 
       #dict3.update({key : dict2[key]})
	else: 
		 dict3.update({key : dict2[key]})		
		
print(dict3) 