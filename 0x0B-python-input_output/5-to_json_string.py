#!/usr/bin/python3
"""
Return a JSON representation of an object
"""


import json


def to_json_string(my_obj):
    """ String JSON representation of the object """
    return json.dumps(my_obj)
