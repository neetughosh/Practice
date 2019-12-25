# -*- coding: utf-8 -*-
"""
Created on Fri Aug 23 22:23:48 2019

@author: NGH5KOR
"""

#!/bin/python3

# Complete the staircase function below.
def staircase(n):
    for i in range(1,n+1):
        print(" "*(n-i) + "#"*i)

if __name__ == '__main__':
    n = int(input())

    staircase(n)