#!/usr/bin/python3
""" Defining a class square """

class Square:
    """ The square class
    Attributes:
    __size : size of a side of the square
    """
    def __init__(self, size=0):
        """ Initialize the square
        Arguments:
             size : side of a side of the square
        Return : None
        """
        if type(size) is int:
            if size < 0:
                raise ValueError("Size must be >= 0")
            else:
                self.__size = size
        else:
            raise TypeError("Size must be an integer")

    def area(self):
        """ Public method that finds the area
        of the square
        
        Return: The area of the square
        """
        return self.__size * self.__size
