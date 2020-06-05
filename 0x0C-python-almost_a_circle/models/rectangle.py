#!/usr/bin/python3
"""
A rectangle class content
"""


from models.base import Base


class Rectangle(Base):
    """ A Rectangle class that inherits from Base """
    def __init__(self, width, height, x=0, y=0, id=None):
        """ Initialize variables """
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

    def area(self):
        """ Method that returns the area of the rectangle """
        return self.__width * self.__height

    def display(self):
        """ Method that prints in stdout the rectangle instance with
        char # """
        rep = "#"
        for space in range(self.__y):
            print()
        for rows in range(self.__height):
            for space in range(self.__x):
                print(" ",end="")
            for cols in range(self.__width):
                print(rep, end="")
            print()

    def __str__(self):
        """ String representation """
        return "[Rectangle] ({}) {}/{} - {}/{}".format(self.id, self.__x, self.__y,
                                                self.__width, self.__height)

    def update(self, *args, **kwargs):
        """ Assigns an argument to each attribute """
        if len(args):
            try:
                self.id = args[0]
                self.width = args[1]
                self.height = args[2]
                self.x = args[3]
                self.y = args[4]
            except:
                pass
        else:
            if "id" in kwargs:
                self.id = kwargs["id"]
            if "width" in kwargs:
                self.width = kwargs["width"]
            if "height" in kwargs:
                self.height = kwargs["height"]
            if "x" in kwargs:
                self.x = kwargs["x"]
            if "y" in kwargs:
                self.y = kwargs["y"]
