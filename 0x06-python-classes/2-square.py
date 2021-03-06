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
            if size < 0:
                raise ValueError("size must be >= 0")
            else:
                self.__size = size
        else:
            raise TypeError("size must be an integer")
