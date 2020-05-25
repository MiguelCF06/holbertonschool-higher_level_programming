#!/usr/bin/python3
""" Create a rectangle class """


class Rectangle:
    """ The rectangle class """
    def __init__(self, width=0, height=0):
        self.width = width
        self.height = height

    @property
    def width(self):
        """ Getter of width """
        return self.__width

    @width.setter
    def width(self, value):
        """ Setter of width """
        if not isinstance(value, int):
            raise TypeError("width must be an integer")
        else:
            if value < 0:
                raise ValueError("width must be >= 0")
        self.__width = value

    @property
    def height(self):
        """ Getter of height """
        return self.__height

    @height.setter
    def height(self, value):
        """ Setter of height """
        if not isinstance(value, int):
            raise TypeError("height must be an integer")
        else:
            if value < 0:
                raise ValueError("height must be >= 0")
        self.__height = value

    def area(self):
        """ Area of the rectangle """
        return self.__width * self.__height

    def perimeter(self):
        """ Rectangle perimeter """
        if self.__width == 0 or self.__height == 0:
            return 0
        else:
            return (self.__width * 2) + (self.__height * 2)
