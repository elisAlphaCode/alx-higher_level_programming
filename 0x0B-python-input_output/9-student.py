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

    def to_json(self):
        return self.__dict__
