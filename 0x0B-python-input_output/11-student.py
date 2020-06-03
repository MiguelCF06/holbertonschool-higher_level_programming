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

    def to_json(self):
        """ Returns a dictionary representation of the class """
        return self.__dict__
