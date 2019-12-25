# -*- coding: utf-8 -*-
"""
Created on Sat Aug 24 09:05:47 2019

@author: NGH5KOR
"""

def miniMaxSum(arr):
    arr.sort()
    n = len(arr)
    print(str(sum(arr[:n-1])) + " " + str(sum(arr[::-1][:n-1])))

if __name__ == '__main__':
    arr = list(map(int, input().rstrip().split()))

    miniMaxSum(arr)
