#!/bin/python3

def JumpOnClouds(clouds):
    numOfJumps = 0
    skipCount = False
    for x in range(len(clouds)):
        print('loop')
        if skipCount:
            skipCount = False
            print("pass")
            continue
        if x < len(clouds) - 2 and clouds[x+2] == 0:
            skipCount = True
            numOfJumps = numOfJumps + 1
            print("num of jumps", numOfJumps)
            print("index", x)
        elif x < len(clouds) - 1 and clouds[x+1] == 0:
            numOfJumps = numOfJumps + 1
            print("num of jumps", numOfJumps)
            print("index", x)
        else:
            break
    print(numOfJumps)

if __name__ == '__main__':
    numOfClouds = int(input("How many clouds"))
    clouds = []
    for x in range(numOfClouds):
        clouds.append(int(input("0 or 1 (safe or not)")))

    JumpOnClouds(clouds)
