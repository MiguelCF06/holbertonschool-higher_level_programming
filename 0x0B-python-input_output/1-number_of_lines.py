#!/usr/bin/python3
"""
Return number of lines of a text
"""

def number_of_lines(filename=""):
    """ Count the amount of lines of the txt file """
    num = 0
    with open(filename, "r") as f:
        for lines in f:
            num += 1
        return num
