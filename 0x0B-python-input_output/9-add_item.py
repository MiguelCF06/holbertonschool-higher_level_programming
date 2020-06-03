#!/usr/bin/python3
"""
Adds all the arguments to a Python list and save them
"""
from sys import argv
save_to_json_file = __import__('7-save_to_json_file').save_to_json_file
load_from_json_file = __import__("8-load_from_json_file").load_from_json_file

filename = "add_item.json"

try:
    myList = load_from_json_file(filename)
except:
    myList = []

for arguments in argv[1:]:
    myList.append(arguments)

save_to_json_file(myList, filename)
