#!/usr/bin/python3
import json
"""
Returns an object represented by a JSON string
"""

def from_json_string(my_str):
    """ Object represented by JSON string """
    return json.loads(my_str)
