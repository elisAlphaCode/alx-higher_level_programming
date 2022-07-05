#!/usr/bin/python3
""" module with the class BaseGeometry """


class BaseGeometry:
    """
    Class that contains area
    """

    @classmethod
    def area(self):
        """ method that raises an exception """

        raise Exception("area() is not implemented")

    def integer_validator(self, name, value):
        """ methods that validates both value """

        if type(value) != int:
            raise TypeError("{} must be an integer".format(name))

        if value <= 0:
            raise ValueError("{} must be greater than 0".format(name))
