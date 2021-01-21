#!/usr/bin/python3
"""here it's the function save_to_json_file"""

import json


def save_to_json_file(my_obj, filename):
    """writes an Object to a text file, using a JSON representation"""
    if (filename != ""):
        with open(filename, 'w') as file_w:
            json.dump(my_obj, file_w)
