#!/usr/bin/python3
"""Module for the add_integer function"""


def add_integer(a, b=98):
    """Returns an integer:
    the sum of a and b"""
    if not isinstance(a, int):
        if isinstance(a, float):
            a = int(a)
        else:
            raise TypeError('a must be an integer')
    if not isinstance(b, int):
        if isinstance(b, float):
            b = int(b)
        else:
            raise TypeError('b must be an integer')
    return a + b
