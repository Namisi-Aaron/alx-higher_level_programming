#!/usr/bin/python3
"""append_write module"""
def append_write(filename="", text=""):
    """append_write opens a file for writing(appends test)
    and creates the file if it doesn't exist
    It returns the number of characters written"""

    with open(filename, 'a', encoding="utf-8") as myFile:
        return myFile.write(text)
