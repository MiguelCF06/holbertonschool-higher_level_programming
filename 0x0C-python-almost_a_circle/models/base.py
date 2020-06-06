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
            return []

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

    @staticmethod
    def from_json_string(json_string):
        """ Returns the list of the JSON string
        representation 'json_string'"""
        if json_string is None or len(json_string) == 0:
            return []
        else:
            return json.loads(json_string)


    @classmethod
    def create(cls, **dictionary):
        """ Returns an instance with all attributes
        already set """
        if cls.__name__ == "Rectangle":
            myDummy = cls(1, 1)
        elif cls.__name__ == "Square":
            myDummy = cls(1)
        myDummy.update(**dictionary)
        return myDummy


    @classmethod
    def load_from_file(cls):
        """ Return a list of instances """
        filename = cls.__name__ + ".json"
        listOfInst = []
        try:
            with open(filename, "r") as f:
                listOfInst = cls.from_json_string(f.read())
            for num, val in enumerate(listOfInst):
                listOfInst[num] = cls.create(**listOfInst[num])
        except:
            pass
        return listOfInst
