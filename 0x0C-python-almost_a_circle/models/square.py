#!/usr/bin/python3
"""
Square content
"""


from models.rectangle import Rectangle


class Square(Rectangle):
    """ Class square """
    def __init__(self, size, x=0, y=0, id=None):
        """ Initialize the variables """
        super().__init__(size, size, x, y, id)

    def __str__(self):
        """ String representation """
        return "[Square] ({}) {}/{} - {}".format(self.id, self.x, self.y,
                                                 self.height)
