#!/usr/bin/python3
"""
Prints a square with "#"

"""


def print_square(size):
    """
    An argument size type integer
    representing the size of the square
    """
    if isinstance(size, bool):
        raise TypeError("size must be an integer")
    elif not isinstance(size, int):
        raise TypeError("size must be an integer")
    if size < 0:
        raise ValueError("size must be >= 0")
    if isinstance(size, int):
        for rows in range(size):
            for cols in range(size):
                print("#", end="")
            print()
