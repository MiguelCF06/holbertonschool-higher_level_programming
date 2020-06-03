#!/usr/bin/python3
"""
Appends a string to the end of a text file
"""

def append_write(filename="", text=""):
    """ Open a file in append mode """
    with open(filename, "a") as f:
        numOfChar = f.write(text)
        return numOfChar
