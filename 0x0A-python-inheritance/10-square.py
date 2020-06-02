#!/usr/bin/python3
""" Square Class """
Rectangle = __import__('9-rectangle').Rectangle

class Square(Rectangle):
    """ A class """
    def __init__(self, size):
        """ Instantiation of square """
        self.integer_validator("size", size)
        self.__size = size
        super().__init__(size, size)

    def area(self):
        """ Area of the square """
        return self.__size ** 2
