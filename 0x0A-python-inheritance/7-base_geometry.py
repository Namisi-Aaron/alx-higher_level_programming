#!/usr/bin/python3
"""base_geometry module"""
class BaseGeometry:
    """BaseGeometry class"""
    def area(self):
        """raises the exception that area() isn't implemented"""
        raise Exception('area() is not implemented')

    def integer_validator(self, name, value):
        """validates value type(integer) and its range"""
        self.name = name
        self.value = value
        if not isinstance(value, int):
            raise TypeError('{} must be an integer'.format(self.name))
        if value <= 0:
            raise ValueError('{} must be greater than 0'.format(self.name))
