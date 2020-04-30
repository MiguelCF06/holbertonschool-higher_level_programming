#!/usr/bin/python3
if __name__ == "__main__":


    from sys import argv

    if (len(argv)-1 == 0):
        print("0 arguments.".format(len(argv) - 1))
    elif (len(argv)-1 == 1):
        print("{} argument:".format(len(argv) - 1))
        print("{}: {}".format(len(argv)-1, argv[1]))
    else:
        print("{} arguments:".format(len(argv) - 1))
        j = 1
        while j <= len(argv)-1:
            print("{:d}: {}".format(j, argv[j]))
            j = j + 1
