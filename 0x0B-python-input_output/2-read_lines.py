#!/usr/bin/python3
"""
Reads n lines of a text file
"""


def read_lines(filename="", nb_lines=0):
    """ Open the file and print n lines """
    with open(filename, "r") as f:
        if nb_lines <= 0:
            for lines in f:
                print(lines, end="")
        for i in range(nb_lines):
            lines = f.readline()
            print(lines, end="")
