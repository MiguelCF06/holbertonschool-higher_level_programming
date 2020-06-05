#!/usr/bin/python3
"""
A rectangle class content
"""


from models.base import Base


class Rectangle(Base):
    """ A Rectangle class that inherits from Base """
    def __init__(self, width, height, x=0, y=0, id=None):
        self.width = width
        self.height = height
        self.x = x
        self.y = y
        super().__init__(id)

    @property
    def width(self):
        """ Getter width """
        return self.__width

    @width.setter
    def width(self, value):
        """ Setter width """
        if not isinstance(value, int):
            raise TypeError("width must be an integer")
        if value <= 0:
            raise ValueError("width must be > 0")
        self.__width = value

    @property
    def height(self):
        """ Getter height """
        return self.__height

    @height.setter
    def height(self, value):
        """ Setter height """
        if not isinstance(value, int):
            raise TypeError("height must be an integer")
        if value <= 0:
            raise ValueError("height must be > 0")
        self.__height = value

    @property
    def x(self):
        """ Getter x """
        return self.__x

    @x.setter
    def x(self, value):
        """ Setter x """
        if not isinstance(value, int):
            raise TypeError("x must be an integer")
        if value < 0:
            raise ValueError("x must be >= 0")
        self.__x = value

    @property
    def y(self):
        """ Getter y """
        return self.__y

    @y.setter
    def y(self, value):
        """ Setter y """
        if not isinstance(value, int):
            raise TypeError("y must be an integer")
        if value < 0:
            raise ValueError("y must be >= 0")
        self.__y = value
