#!/usr/bin/python3
""" module that contains is_same_class method """


def is_same_class(obj, a_class):
    """ Method that return True if an object is an instance of a class """

    return (type(obj) == a_class)
