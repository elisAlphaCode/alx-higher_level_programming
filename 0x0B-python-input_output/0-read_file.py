#!/usr/bin/python3
""" Module that contains read_file function """


def read_file(filename=""):
    """ function that reads a text file (UTF-8) and print it to stdout """
    with open(filename, "r", encoding='utf-8') as a_file:

        print(a_file.read(), end="")
