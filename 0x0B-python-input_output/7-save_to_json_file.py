#!/usr/bin/python3
import json
"""
Writes an object to a text file using JSON repr
"""

def save_to_json_file(my_obj, filename):
    """ Open file a writes """
    with open(filename, "w") as f:
        json.dump(my_obj, f)
