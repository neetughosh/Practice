# -*- coding: utf-8 -*-
"""
Created on Mon Sep 23 23:07:31 2019

@author: NGH5KOR
"""
   

#builtin function

# combinations is used to make all possible combinations og the elements in a list
from itertools import combinations
import copy

list_data = []
# Non builtin function
def combination_non_builtin(arr, start, end, data, index, r):
    
    if (index == r):
        list_data.append(copy.deepcopy(data))       
       
    else:
        
        while(start <= end):
            data[index] = arr[start]
            combination_non_builtin(arr, start+1, end, data, index+1, r)
            start += 1
            

def sum_zero(N):
    """
        Returns the combination whose sum of all elements is Zero and doesn't contain duplicates
    """
    
    # create a list from -N to N range
    arr_list = range((-1*N), N+1)
    
    # Run a loop over all combinations of  the list
    for c in combinations(arr_list, N):
        
        # return the combination whose sum of all elements is Zero and doesn't contain duplicates
        if(sum(c)==0 and len(set(c)) == N):
            return c
        
        
#N = 4
#print(sum_zero(4)) 
#print(list(combinations(range((-1*N), N+1), N)))
#N = 3
#print(sum_zero(3))
#N = 2
#print(sum_zero(2))
#N = 1
#print(list(combinations(range((-1*N), N+1), N)))
#print(sum_zero(1))
#
#N = 3
#r= N
#d = [0]*r      
#
#list_arr = range((-1*N), N+1)    
#print(list(list_arr))
#print(combination_non_builtin(list_arr,0,len(list_arr)-1,d,0,r))
#
#print(list(combinations(list_arr, N)))
#
#print("\n\n")
#
#print(list_data)   
            

            

