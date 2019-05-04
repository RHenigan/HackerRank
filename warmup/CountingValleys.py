#!/bin/python3

def countValleys(steps, map):
    elevation = 0
    valleyCount = 0
    outOfValley = True
    for x in range(steps):
        if map[x] == 'U':
            elevation = elevation + 1
        else:
            elevation = elevation - 1

        if elevation < 0:
            if outOfValley:
                valleyCount = valleyCount + 1
            outOfValley = False
        else:
            outOfValley = True
    print(valleyCount)


if __name__ == '__main__':
    steps = int(input("How many steps?"))
    map = input("Map the elevation")
    countValleys(steps, map)