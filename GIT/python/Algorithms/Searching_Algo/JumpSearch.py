# -*- coding: utf-8 -*-
"""
Created on Sun Oct 13 14:12:07 2019

@author: NGH5KOR
"""
import math
import re


result = re.search(r'TP', 'TP Tutorials Point')
print (result.group())

result = re.match(r'TP', 'TP Tutorials Point')
print (result.group())

result = re.findall(r'TP', 'TP Tutorials Point TP')
print (result)


#def JumpSearch(arr, x):
#    
#    jump_nbr = math.floor(pow(len(arr), 0.5))
#    
#    i = 0
#    
#    while 
#    
#    
#
#
#
#
#
#
#
#
#
#
#
#
#arr = [ 0, 1, 1, 2, 3, 5, 8, 13, 21, 
#    34, 55, 89, 144, 233, 377, 610 ] 
#x = 55