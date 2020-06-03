#!/usr/bin/python3
import json
"""
Creates an object from a JSON file
"""

def load_from_json_file(filename):
    with open(filename, "r") as f:
        obj = json.load(f)
        return obj
