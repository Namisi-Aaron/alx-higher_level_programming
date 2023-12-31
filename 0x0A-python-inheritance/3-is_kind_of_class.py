#!/usr/bin/python3
"""This module contains the function is_kind_of_class"""

def is_kind_of_class(obj, a_class):
    """Returns true if obj is an instance of,
    or if obj is an instance of a_class that inherited from,
    the a_class ; otherwise False"""

    return isinstance(obj, a_class)
