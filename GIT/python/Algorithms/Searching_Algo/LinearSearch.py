# -*- coding: utf-8 -*-
"""
Created on Sat Oct 12 16:08:06 2019

@author: NGH5KOR
"""



def linearsearch(arr, x):
    for i in arr:
        if x==i:        
            return arr.index(i)
arr= [10, 20, 80, 30, 60, 50, 110, 100, 130, 170]
x = 65  
result = linearsearch(arr, x)
if result != None:
    print("element is at", result)  
else:
    print("element not found")    