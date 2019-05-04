#!/bin/python3
import math


def repeatedString(s, n):
    numOfA = 0
    remainderA = 0
    print(n%len(s))
    for letterIndex in range(len(s)):
        if s[letterIndex] == 'a':
            if letterIndex <= (n % len(s)) - 1:
                remainderA = remainderA + 1
            numOfA = numOfA + 1
    numOfA = numOfA * math.floor(n/len(s))
    numOfA = numOfA + remainderA
    print(numOfA)





if __name__ == '__main__':
    repeatedString('a', 100000000)
