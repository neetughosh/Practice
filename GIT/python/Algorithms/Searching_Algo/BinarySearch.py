# -*- coding: utf-8 -*-
"""
Created on Sun Oct 13 11:06:27 2019

@author: NGH5KOR
"""

def binary_search(arr,ele, low, high):
    
    while low<=high:
        mid = (low +high)//2
        if ele == arr[mid]:
            return mid
        elif ele < arr[mid]:
            high = mid -1
        else:
            low = mid+1
            
def binary_search_recursion(arr,ele, low, high):
    
    if high>=low:
        mid = (low +high)//2
        if ele == arr[mid]:
            return mid
        elif ele < arr[mid]:
            return binary_search_recursion(arr,ele, low, mid-1)
        else:
            return binary_search_recursion(arr,ele, mid+1, high)           


arr = [ 2, 3, 4, 10, 40 ] 
ele = 10
result = binary_search(arr,ele, 0, len(arr)-1)
result = binary_search_recursion(arr,ele, 0, len(arr)-1)

print(result)