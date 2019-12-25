#!/bin/python

import os

# Complete the countingValleys function below.
def countingValleys(n, s):
    valley = 0
    total = 0
    for i in (s):
        if (i == 'U'): 
            total += 1
        if (i == 'D'):
            total -= 1
        if total == 0 and i == 'U':
            valley += 1
    return valley      

            


if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    n = int(input())

    s = input()

    result = countingValleys(n, s)

    fptr.write(str(result) + '\n')

    fptr.close()
