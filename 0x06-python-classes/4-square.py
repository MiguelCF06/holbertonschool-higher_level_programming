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

        self.__size = size

    @property
    def size(self):
        """ Getter of the __size

        Return: The size of the square
        """

        return self.__size

    @size.setter
    def size(self, value):
        """setter of __size

        Args:
            value: the size of a size of the square

        Returns: None
        """

        if type(value) is int:
            if value < 0:
                raise ValueError("size must be >= 0")
            else:
                self.__size = value
        else:
            raise TypeError("size must be an integer")

    def area(self):
        """ Public method that finds the area
        of the square

        Return: The area of the square
        """

        return self.__size * self.__size
