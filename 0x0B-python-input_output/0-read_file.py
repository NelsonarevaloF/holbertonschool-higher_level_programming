#!/usr/bin/python3
"""here it's the function read_file"""


def read_file(filename=""):
    """read a text file and prints it to stdout"""
    if (filename != ""):
        with open(filename) as f:
            for line in f:
                print(line, end="")
        print()
