#!/usr/bin/python3
""" Inherits function """
def inherits_from(obj, a_class):
    """ Return True or false """
    return (issubclass(type(obj), a_class) and type(obj) != a_class)
