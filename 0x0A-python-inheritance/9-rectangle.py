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

    def area(self):
        """ Return the area of the rectangle """
        return self.__width * self.__height

    def __str__(self):
        """ String representation """
        return("[Rectangle] {}/{}".format(self.__width, self.__height))
