#!/usr/bin/python3
""" Defining a class Square """


class Square:
    """ The square class

    Attributes:
    __size : size of a side of the square
    __position : position of the square
    """
    def __init__(self, size=0, position=(0, 0)):
        """ Initialize the square

        Arguments:
             size : side of a side of the square
             position : the of the square

        Return : None
        """
        self.size = size
        self.position = position

    @property
    def size(self):
        """ Getter of the __size

        Returns: The size of the square
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

    @property
    def position(self):
        """getter of __position

        Returns:
            The position of the square in 2D space
        """
        return self.__position

    @position.setter
    def position(self, value):
        """setter of __position

        Args:
            value (tuple): position of the square in 2D space

        Returns:
            None
        """
        if type(value) is not tuple or len(value) != 2 or \
           type(value[0]) is not int or value[0] < 0 or \
           type(value[1]) is not int or value[1] < 0:
            raise TypeError("position must be a tuple of 2 positive integers")
        else:
            self.__position = value


    def area(self):
        """ Public method that finds the area
        of the square

        Returns: The area of the square
        """
        return self.__size * self.__size

    def my_print(self):
        """ Public method that prints the size of the square
        with # and spaces

        Return: none
        """
        if self.__size == 0:
            print()
            return
        else:
            if self.__position[0] >= 0 and self.__position[1] >= 0:
                for lines in range(self.__position[1]):
                    print()
            for rows in range(self.__size):
                if self.__position[1] >= 0:
                    for spaces in range(self.__position[0]):
                        print(" ", end="")
                for spaces in range(self.__position[0]):
                    print(" ", end="")
                for cols in range(self.__size):
                    print("#", end="")
                print()
