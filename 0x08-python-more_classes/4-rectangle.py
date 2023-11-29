#!/usr/bin/python3
"""This module creates a class Rectangle"""
class Rectangle:
    """This is a class Rectangle"""

    def __init__(self, width=0, height=0):
        """The __init__ method

        Attributes:
            width: the width of the rectangle.
            height: the height of the rectangle
        """
        self.__width = width
        self.__height = height

    @property
    def width(self):
        """This is the width getter method"""
        return self.__width

    @width.setter
    def width(self, value):
        if not isinstance(value, int):
            raise TypeError('width must be an integer')
        if value < 0:
            raise ValueError('width must be >= 0')
        self.__width = value

    @property
    def height(self):
        """This is the height getter method"""
        return self.__height

    @height.setter
    def height(self, value):
        if not isinstance(value, int):
            raise TypeError('height must be an integer')
        if value < 0:
            raise ValueError('height must be >= 0')
        self.__height = value

    def area(self):
        """Returns the rectangle's area"""
        return self.__height * self.__width

    def perimeter(self):
        """Returns the perimeter of the rectangle"""
        if self.__height == 0 or self.__width == 0:
            return 0
        else:
            return 2 * (self.__height + self.__width)

    def __str__(self):
        rect_string = ''
        if self.__height == 0 or self.__width == 0:
            return ''
        else:
            for i in range(0, self.__height):
                rect_string += '#' * self.__width + '\n'
        return rect_string

    def __repr__(self):
        return 'Rectangle(width={}, height={})'.format(
                self.__width, self.__height)
