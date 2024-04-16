#!/usr/bin/python3
"""Contains the function append_write"""


def append_write(filename="", text=""):
    """Appends a string to the end of a text file"""
    with open(filename, 'a', encoding='utf-8') as f:
        return f.write(text)
