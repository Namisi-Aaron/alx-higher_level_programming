#!/usr/bin/python3
"""Defines the class BaseGeometry"""


class BaseGeometry:
    """Is an empty class"""
    def __init__(self):
        pass

    def area(self):
        raise Exception("area() is not implemented")
