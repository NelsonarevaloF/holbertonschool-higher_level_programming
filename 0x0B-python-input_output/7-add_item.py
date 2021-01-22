#!/usr/bin/python3
"""here it's the function load_from_json_file"""

import sys


load_from_json_file = __import__('6-load_from_json_file').load_from_json_file
save_to_json_file = __import__('5-save_to_json_file').save_to_json_file

path = "add_item.json"
try:
    f_return = load_from_json_file(path)
except:
    f_return = []
for item in sys.argv[1:]:
    f_return.append(item)
save_to_json_file(f_return, path)
