#!/usr/bin/python3
"""Module for the inherits from function"""

def inherits_from(obj, a_class):
    """inherits from returns true if the object ia an instance
    of a class the inherited fro the specified class
    Otherwise False"""

    if issubclass(type(obj), a_class):
        if not type(obj) is a_class:
            return True
    return False
