#!/usr/bin/python3
""" module with the class BaseGeometry """

BaseGeometry = __import__('7-base_geometry').BaseGeometry


class Rectangle(BaseGeometry):
    """class Rectangle inherits from BaseGeometry"""

    def __init__(self, width, height):
        """initialization of privates"""
        self.integer_validator('width', width)
        self.__width = width
        self.integer_validator('height', height)
        self.__height = height

    def area(self):
        """ method that prints the area of a rectangle """
        return self.__height * self.__width

    def __str__(self):
        """
        method that returns the implementation of
        the class in string format
        """

        return "[Rectangle] {}/{}".format(self.__width, self.__height)
