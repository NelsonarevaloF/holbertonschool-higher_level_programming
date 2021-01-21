#!/usr/bin/python3
"""here it's the function write_file"""


def write_file(filename="", text=""):
    """writes a string to a text file and returns
    the number of characters written"""
    if (filename != "" and text != ""):
        with open(filename, 'w') as f:
                q_bytes = f.write(text)
        return (q_bytes)
