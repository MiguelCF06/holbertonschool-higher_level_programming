#!/usr/bin/python3
""" Class Rectangle """
BaseGeometry = __import__('7-base_geometry').BaseGeometry

class Rectangle(BaseGeometry):
    """ A class which inherite from BaseGeometry """
    def __init__(self, width, height):
        """ Instantiation of the rectangle """
        self.integer_validator("width", width)
        self.__width = width
        self.integer_validator("height", height)
        self.__height = height
