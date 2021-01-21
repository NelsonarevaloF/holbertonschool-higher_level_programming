#!/usr/bin/python3
"""here it's the function load_from_json_file"""

import json


def load_from_json_file(filename):
    """create an Object from a “JSON file”"""
    if (filename != ""):
        with open(filename) as file_r:
            object_python = json.load(file_r)
        return object_python
