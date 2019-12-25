# -*- coding: utf-8 -*-
"""
Created on Sat Aug 31 18:23:31 2019

@author: NGH5KOR
"""

if __name__ == '__main__':
    n = int(input())

maxseq = 0
count = 0

binary=[]
while (n>0):
    rem = n%2
    binary.append(rem)
    n = n//2
    
    if(rem == 1):
        count += 1
    if(rem == 0):
        count = 0
        
    maxseq = max(maxseq, count)    
    
    
print(maxseq)   