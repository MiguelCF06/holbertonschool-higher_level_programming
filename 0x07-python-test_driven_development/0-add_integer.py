#!/usr/bin/python3
"""
Adds two integers (a and b)

Returns the result
"""


def add_integer(a, b=98):
    """
    2 parameters a and b to add them
    """
    if type(a) not in [int, float]:
        raise TypeError("a must be an integer")
    elif type(b) not in [int, float]:
        raise TypeError("b must be an integer")

    return int(a)+int(b)
