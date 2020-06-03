#!/usr/bin/python3
"""
Inserts a line of text to a file.
"""


def append_after(filename="", search_string="", new_string=""):
    """ Appends a string to a text file """
    with open(filename, "r") as f:
        listOfLine = []
        while True:
            line = f.readline()
            if line == "":
                break
            listOfLine.append(line)
            if search_string in line:
                listOfLine.append(new_string)
    with open(filename, "w") as f:
        f.writelines(listOfLine)
