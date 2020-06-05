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
        self.__width = value

    @property
    def height(self):
        """ Getter height """
        return self.__height

    @height.setter
    def height(self, value):
        """ Setter height """
        self.__height = value

    @property
    def x(self):
        """ Getter x """
        return self.__x

    @x.setter
    def x(self, value):
        """ Setter x """
        self.__x = value

    @property
    def y(self):
        """ Getter y """
        return self.__y

    @y.setter
    def y(self, value):
        """ Setter y """
        self.__y = value
