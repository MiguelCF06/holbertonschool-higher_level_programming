#!/usr/bin/python3
"""
Class content
"""


import json


class Base:
    """ The base class """
    __nb_objects = 0
    def __init__(self, id=None):
        """ Initialize variables """
        if id is not None:
            self.id = id
        else:
            Base.__nb_objects += 1
            self.id = Base.__nb_objects

    def to_json_string(list_dictionaries):
        """ Returns the JSON string representation of
        list__dictionaries """
        if len(list_dictionaries):
            return json.dumps(list_dictionaries)
        else:
            return "[]"
