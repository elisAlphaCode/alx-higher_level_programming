#!/usr/bin/python3
""" module that contains the class Student """


class Student:
    """
    A class of student and method to_json
    Attributes:
        first_name (str): name of student.
        last_name (str): name of student.
        age (int): age of student.
    Methods:
        __init__ - initializes the Student instance.
        to_json - retrieves dictionary repr of Student instance.
    """
    def __init__(self, first_name, last_name, age):
        """ initializing first_name, last_name and age """
        self.first_name = first_name
        self.last_name = last_name
        self.age = age

    def to_json(self, attr=None):
        """
            retrieves a dictionary representation of Student.
            Args:
            attr (list): attribute names that are to be retrieved.
        """
        if attr is not None:
            res = {k: self.__dict__[k] for k in self.__dict__.keys() & attr}
            return res
        else:
            return self.__dict__

    def reload_from_json(self, json):
        '''Loads attributes from json.'''
        for key, value in json.items():
            self.__dict__[key] = value
