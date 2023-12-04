#!/usr/bin/python3
class BaseGeometry:
    """BaseGeometry class"""

    def area(self):
        """Raises the exception that area() isn't implemented"""
        raise Exception('area() is not implemented')

    def integer_validator(self, name, value):
        """Validates value type (integer) and its range"""
        if not isinstance(value, int):
            raise TypeError('{} must be an integer'.format(name))
        if value <= 0:
            raise ValueError('{} must be greater than 0'.format(name))

class Rectangle(BaseGeometry):
    """Subclass Rectangle"""
    def __init__(self, width, height):
        """Instantiation with width and height
        width and height are validated by integer_validator"""

        self.integer_validator('width', width)
        self.__width = width
        self.integer_validator('height', height)
        self.__height = height
