#!/usr/bin/python3
""" A class mylist that inherit from list """

class MyList(list):
    """Print the list in a sorted
    way
    """
    def print_sorted(self):
        for num in self:
            if isinstance(num, int):
                print(sorted(self))
                break
