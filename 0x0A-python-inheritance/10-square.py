#!/usr/bin/python3
""" module with the class BaseGeometry """

Rectangle = __import__("9-rectangle").Rectangle


class Square(Rectangle):
    """Class Square inherits from Rectangle"""
    def __init__(self, size):
        """initializer"""
        super().__init__(size, size)
        self.integer_validator('size', size)
        self.__size = size
