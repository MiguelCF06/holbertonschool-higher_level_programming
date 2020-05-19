#!/usr/bin/python3
""" Defining a class Square """
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
            self.__size = size
            if size < 0:
                raise ValueError("Size must be >= 0")
        else:
            raise TypeError("Size must be an integer")
