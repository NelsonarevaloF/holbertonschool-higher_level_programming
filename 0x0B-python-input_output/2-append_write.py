#!/usr/bin/python3
"""here it's the function write_file"""


def append_write(filename="", text=""):
    """appends a string at the end of a text file
    and returns the number of characters added"""
    if (filename != "" and text != ""):
        with open(filename, 'a') as f:
                q_bytes = f.write(text)
        return (q_bytes)
