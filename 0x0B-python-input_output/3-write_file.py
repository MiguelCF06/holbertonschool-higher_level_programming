#!/usr/bin/python3
"""
Writes a string to a txt file
"""


def write_file(filename="", text=""):
    """ Open a file in write mode """
    with open(filename, "w") as f:
        numOfChar = f.write(text)
        return numOfChar
