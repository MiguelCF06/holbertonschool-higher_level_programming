#!/usr/bin/python3
""" Class definitio """

class MyInt(int):
    """ A class """
    def __eq__(self, oth):
        """ Override the == operator """
        return int(self) != oth
    
    def __ne__(self, oth):
        """ Override the != operator """
        return int(self) == oth
