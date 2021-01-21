#!/usr/bin/python3
import json
"""here it's the function from_json_string"""


def from_json_string(my_str):
    """return an object (Python data structure) represented by a JSON string"""
    return (json.loads(my_str))
