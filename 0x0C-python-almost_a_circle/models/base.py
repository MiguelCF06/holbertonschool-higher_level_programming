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

    @staticmethod
    def to_json_string(list_dictionaries):
        """ Returns the JSON string representation of
        list__dictionaries """
        if len(list_dictionaries):
            return json.dumps(list_dictionaries)
        else:
            return "[]"

    @classmethod
    def save_to_file(cls, list_objs):
        """ Writes the JSON string of list_objs to
        a file """
        filename = cls.__name__ + ".json"
        listOfDict = []
        if list_objs is not None:
            for objs in list_objs:
                listOfDict.append(cls.to_dictionary(objs))
        with open(filename, "w") as f:
            f.write(cls.to_json_string(listOfDict))
