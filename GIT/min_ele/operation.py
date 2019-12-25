# -*- coding: utf-8 -*-
"""
Created on Fri Sep 2019

@author: Neetu Ghosh
"""

"""

Given an array of elements that provide a less than operator, Find the minimum using as few comparisons as possible.
The array shall be given such that the first few elements are monotonically decreasing and remaining elements are strictly monotonically increasing.

"""
        
def binary_search(arr, low, high):
    """    
    Purpose : This function find the smallest element using Binary search
    
    Input : 
        arr  : The array from which the smallest element has to be returned
        low  : Starting index of the array
        high : End index of the array  
        
    Output : Smallest element in the array 
    """ 
    
    # Check for empty array
    if (low > high):
        raise IndexError('Array is empty')
    
    # Finds the smallest element
    while(low < high):
        mid = (low + (high-low)//2)
        
        if arr[mid] < arr[mid+1]:
            high = mid
        else:
            low = mid + 1
    return arr[low]        
        
def minimum(array):
    """    
    Purpose : This function returns the minimum element in an array
    
    Input   : 
        array  : The array from which the smallest element has to be returned
        
    Output  : Smallest element in an array
    
    """   
    
    arr_len = len(array)
    low = 0
    high = arr_len-1
    
    return binary_search(array, low, high)
        