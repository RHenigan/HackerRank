#!/bin/python3
import math


def sockMerchant(n, ar):
    ar.sort()
    startSock = ar[0]
    currSockCount = 0
    pairs = 0
    for x in range(n):
        if ar[x] == startSock:
            currSockCount = currSockCount + 1
        else:
            startSock = ar[x]
            pairs = math.floor(pairs + currSockCount / 2)
            currSockCount = 1
    pairs = math.floor(pairs + currSockCount / 2)
    print(pairs)

if __name__ == '__main__':
    num_of_socks = int(input("How many socks"))
    socks = []
    for x in range(num_of_socks):
        socks.append(int(input("Socks size")))

    sockMerchant(num_of_socks, socks)