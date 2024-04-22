#!/usr/bin/python3
"""Contains the function is_same_class"""


def is_same_class(obj, a_class):
    """Checks if an object is an instance of a specified class"""
    if (isinstance(obj, a_class) and type(obj) is a_class):
        return True
    return False
