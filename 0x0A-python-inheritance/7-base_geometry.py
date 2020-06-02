#!/usr/bin/python3
""" Definition of a class """

class BaseGeometry():
    """ A class """
    def area(self):
        """ Raises an exception """
        raise Exception("area() is not implemented")

    def integer_validator(self, name, value):
        """ Validate the base geometry """
        if isinstance(name, str):
            if not isinstance(value, int):
                raise TypeError("{} must be an integer".format(name))
            if value <= 0:
                raise ValueError("{} must be greater than 0".format(name))
