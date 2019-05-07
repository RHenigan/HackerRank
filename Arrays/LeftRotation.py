#!/bin/python3


def rotLeft(arr, d):
    for i in range(d):
        arr.append(arr[0])
        arr.pop(0)
    print(arr)

if __name__ == '__main__':
    arr = [1, 2, 3, 4, 5]

    rotLeft(arr, 4)
