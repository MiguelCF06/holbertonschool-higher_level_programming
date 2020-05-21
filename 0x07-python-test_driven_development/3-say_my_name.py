#!/usr/bin/python3
"""
Print name with format
"""


def say_my_name(first_name, last_name=""):
    """
    2 parameters first name and last name must be strings
    """
    if isinstance(first_name, str) and isinstance(last_name,str):
        print("My name is {} {}".format(first_name, last_name))
    if not isinstance(first_name, str):
              raise TypeError("first_name must be a string")
    if not isinstance(last_name, str):
              raise TypeError("last_name must be a string")
