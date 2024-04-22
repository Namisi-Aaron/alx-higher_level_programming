#!/usr/bin/python3
"""Defines the class BaseGeometry and Rectangle"""


class BaseGeometry:
    """Is an empty class"""
    def __init__(self):
        pass

    def area(self):
        raise Exception("area() is not implemented")

    def integer_validator(self, name, value):
        if type(value) is not int:
            raise TypeError("{} must be an integer".format(name))
        if value <= 0:
            raise ValueError("{} must be greater than 0".format(name))


class Rectangle(BaseGeometry):
    """Defines the class Rectangle that inherits from BaseGeometry"""
    def __init__(self, width, height):
        super().integer_validator(name='width', value=width)
        super().integer_validator(name='height', value=height)
        self.__width = width
        self.__height = height
