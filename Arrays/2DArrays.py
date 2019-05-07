#!/bin/python3

def countHourGlass(i, j, arr):
    hgSum = 0
    hgSum = hgSum + arr[i][j] + arr[i][j + 1] + arr[i][j + 2]
    hgSum = hgSum + arr[i + 1][j + 1]
    hgSum = hgSum + arr[i + 2][j] + arr[i + 2][j + 1] + arr[i + 2][j + 2]
    return hgSum

def hourglassSum(arr):
    result = 0
    for i in range(4):
        for j in range(4):
            tempResult = countHourGlass(i, j, arr)
            if tempResult > result or (i == 0 and j == 0):
                result = tempResult
    print(result)

if __name__ == '__main__':
    arr = [[1, 1, 1, 1, 1, 1],
           [3, 3, 3, 3, 3, 3],
           [3, 3, 3, 3, 3, 3],
           [4, 4, 4, 4, 4, 4],
           [5, 5, 5, 5, 5, 5],
           [6, 6, 6, 6, 6, 6]]

    hourglassSum(arr)