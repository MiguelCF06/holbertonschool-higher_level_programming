#!/usr/bin/python3
"""
Reads a file
"""


def read_file(filename=""):
    """ Open a file, read, and print it """
    with open(filename, "r") as f:
        for line in f:
            print(line, end="")
