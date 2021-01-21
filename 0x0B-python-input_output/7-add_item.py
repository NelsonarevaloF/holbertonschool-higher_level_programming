#!/usr/bin/python3
"""here it's the function load_from_json_file"""

import sys


load_from_json_file = __import__('6-load_from_json_file').load_from_json_file
save_to_json_file = __import__('5-save_to_json_file').save_to_json_file

path = "add_item.json"
try:
    f = open(path, 'x')
    save_to_json_file([], path)
except:
    list_return = load_from_json_file(path)
    for arg in sys.argv[1:]:
        list_return.append(arg)
    save_to_json_file(list_return, path)
