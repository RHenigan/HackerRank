#!/bin/python3


def rotLeft(arr, d):
    output = []
    for i in range(len(arr)):
        newIndex = (i - d) % len(arr)
        output.insert(newIndex, arr[i])
    print(arr)

if __name__ == '__main__':
    arr = [1, 2, 3, 4, 5]

    rotLeft(arr, 4)
