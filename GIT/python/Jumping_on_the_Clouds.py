#!/bin/python

import os

# Complete the jumpingOnClouds function below.
def jumpingOnClouds(c):

    #0 0 0 0 1 0
    count = 0
    length = len(c)
    i = 0
    while(i<length):
        if(c[i] == 0):
            if i+2 < length and c[i] == c[i+2]:
                i += 2
                count += 1
                continue
            count += 1
            i += 1
            continue
        i +=1    
    return count-1         
            
if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    n = int(input())

    c = map(int, input().rstrip().split())

    result = jumpingOnClouds(c)

    fptr.write(str(result) + '\n')

    fptr.close()
