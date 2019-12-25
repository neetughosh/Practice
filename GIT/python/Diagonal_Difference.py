# -*- coding: utf-8 -*-
"""
Created on Fri Aug 23 22:23:00 2019

@author: NGH5KOR
"""

#!/bin/python3

import os

#
# Complete the 'diagonalDifference' function below.
#
# The function is expected to return an INTEGER.
# The function accepts 2D_INTEGER_ARRAY arr as parameter.
#

def diagonalDifference(arr):
    # Write your code here
    diag_sum = 0
    n = len(arr)
    
    for i in range(n):
        diag_sum = arr[i][i] - arr[i][n-i-1]
    return abs(diag_sum)    

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    n = int(input().strip())

    arr = []

    for _ in range(n):
        arr.append(list(map(int, input().rstrip().split())))

    result = diagonalDifference(arr)

    fptr.write(str(result) + '\n')

    fptr.close()
