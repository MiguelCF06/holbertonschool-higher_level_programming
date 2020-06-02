#!/usr/bin/python3
""" Definition of function that verifies
if the object is an instance of, or if the
object is an instance of a class that
inherited from, the specified class
"""
def is_kind_of_class(obj, a_class):
    """ Return True or False """
    return isinstance(obj, a_class)
