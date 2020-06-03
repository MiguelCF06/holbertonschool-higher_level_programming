#!/usr/bin/python3
"""
Returns a dictionary description with simple data structure
"""

def class_to_json(obj):
    """ Makes the dictionary for JSON serialization of an obj """
    return obj.__dict__
