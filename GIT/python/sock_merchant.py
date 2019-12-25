#!/bin/python

import os
import collections

# Complete the sockMerchant function below.
def sockMerchant(n, ar):
    freq = collections.Counter(ar)
    socks_total = 0
    for key, val in (freq.iteritems()):
        socks_total += (val/2)

    return socks_total

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    n = int(input())

    ar = map(int, input().rstrip().split())

    result = sockMerchant(n, ar)

    fptr.write(str(result) + '\n')

    fptr.close()
