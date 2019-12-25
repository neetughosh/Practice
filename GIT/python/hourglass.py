#!/bin/python3
def total(arr, i, j):
    return arr[i][j] + arr[i][j+1] + arr[i][j+2] + arr[i+1][j+1] + arr[i+2][j] + arr[i+2][j+1] + arr[i+2][j+2]

if __name__ == '__main__':
    arr =[]
    n = 6
    total_sum = -999999999999999999999999999999999999999
    for _ in range(6):
        arr.append(list(map(int, input().rstrip().split())))

    n = len(arr)        
    for i in range(0,n-2):
        for j in range(0,n-2):
            total_sum = max(total(arr, i, j), total_sum)
    print(total_sum)            