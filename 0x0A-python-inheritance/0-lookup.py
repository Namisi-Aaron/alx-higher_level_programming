#!/usr/bin/python3
"""This module defines a function lookup"""

def lookup(obj):
    """returns the list of available
    attributes and methods of an object

    Args:
        obj: the object to be checked
    """

    return dir(obj)
