#!/usr/bin/python3
if __name__ == "__main__":
    from sys import argv

    if (len(argv)-1 == 0):
        print(0)
    elif (len(argv)-1 > 0):
        Sum = 0
        n = len(argv)
        for x in range(1, n):
            Sum += int(argv[x])
        print(Sum)
