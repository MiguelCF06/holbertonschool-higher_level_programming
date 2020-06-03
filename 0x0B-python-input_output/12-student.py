#!/usr/bin/python3
"""
Class Student content
"""


class Student:
    """ A student class """
    def __init__(self, first_name, last_name, age):
        """ initialize the class """
        self.first_name = first_name
        self.last_name = last_name
        self.age = age

    def to_json(self, attrs=None):
        """ Returns a dictionary representation of the class """
        if attrs is None:
            return self.__dict__
        myDict = {}
        for atribute in attrs:
            try:
                myDict[atribute] = self.__dict__[atribute]
            except:
                pass
        return myDict
