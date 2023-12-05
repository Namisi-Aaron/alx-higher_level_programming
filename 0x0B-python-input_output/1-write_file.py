#!/usr/bin/python3
"""write_file module"""
def write_file(filename="", text=""):
    """This module writes a string text
    and returns the number of characters written"""

    with open(filename, 'w', encoding="utf-8") as myFile:
        return myFile.write(text)
