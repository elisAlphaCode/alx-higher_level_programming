#!/usr/bin/python3
"""
Module for Base class
"""


import json
import turtle
import csv


class Base:
    """
    Base - class defining another classes
    """
    __nb_objects = 0

    def __init__(self, id=None):
        """
        Constructor of Base
        """
        if id is not None:
            self.id = id
        else:
            Base.__nb_objects += 1
            self.id = Base.__nb_objects

    @staticmethod
    def to_json_string(list_dictionaries):
        """
        Returns the JSON string representation of a list
        Arguments:
        @list_dictionaries: is a list of dictionaries
        Returns:
        The JSON string representation of list_dictionaries, otherwise "[]"
        """
        if list_dictionaries is None or len(list_dictionaries) == 0:
            return '[]'
        else:
            return json.dumps(list_dictionaries)

    @classmethod
    def save_to_file(cls, list_objs):
        """
        Writes the JSON string representation of list_objs to a file
        Arguments:
        @cls: class
        @list_objs: is a list of instances who inherits of Base
        Returns:
        Only writes the JSON string in the file
        """
        with open('{}.json'.format(cls.__name__), 'w') as f:
            if list_objs is None:
                f.write(cls.to_json_string([]))
            else:
                jlist = []
                for i in list_objs:
                    i = i.to_dictionary()
                    jlist.append(i)
                f.write(cls.to_json_string(jlist))

    @staticmethod
    def from_json_string(json_string):
        """
        Converts a dictionary to a JSON string representation
        Arguments:
        @json_string: is a string representing a list of dictionaries
        Returns:
        list of JSON string representation, otherwise a empty list
        """
        if json_string is None or len(json_string) == 0:
            return []
        else:
            return json.loads(json_string)

    @classmethod
    def create(cls, **dictionary):
        """
        Returns an instance with all attributes already set
        Arguments:
        @cls: current class
        @dictionary: can be thought of as a double pointer to a dictionary
        Returns:
        An instance with all attributes already set
        """
        if cls.__name__ == "Rectangle":
            new = cls(1, 1, 0, 0)
        elif cls.__name__ == "Square":
            new = cls(1, 0, 0)
        new.update(**dictionary)
        return new

    @classmethod
    def load_from_file(cls):
        """
        Return a list of instances
        Arguments:
        @cls: current class
        Returns:
        An empty list if the file does not exist, otherwise,
        return a list of instances, the type of these instances depends on cls
        """
        try:
            with open('{}.json'.format(cls.__name__), encoding='utf-8') as f:
                jtext = f.read()
                new_object = cls.from_json_string(jtext)
                new_list = []
                for i in new_object:
                    new_list.append(cls.create(**i))
                return new_list
        except FileNotFoundError:
            return []

    @classmethod
    def save_to_file_csv(cls, list_objs):
        """
        save_to_file_csv - serializes in CVS
        """
        filename = cls.__name__ + ".csv"
        if filename == "Rectangle.csv":
            fields = ["id", "width", "height", "x", "y"]
        else:
            fields = ["id", "size", "x", "y"]
        with open(filename, mode="w", newline="") as f:
            if list_objs is None:
                writer = csv.writer(f)
                writer.writerow([[]])
            else:
                writer = csv.DictWriter(f, fieldnames=fields)
                writer.writeheader()
                for x in list_objs:
                    writer.writerow(x.to_dictionary())

    @classmethod
    def load_from_file_csv(cls):
        """
        load_from_file_csv - deserializes from csv
        """
        try:
            with open('{}.csv'.format(cls.__name__), newline="") as f:
                reader = csv.DictReader(f)
                my_list = []
                for x in reader:
                    for i, n in x.items():
                        x[i] = int(n)
                    my_list.append(x)
                return ([cls.create(**objt) for objt in my_list])
        except FileNotFoundError:
            return ([])

    @staticmethod
    def draw(list_rectangles, list_squares):
        """
        draw - Draws squares and rectangles
        """
        my_turtle = turtle.Turtle()
        for r in list_rectangles:
            my_turtle.setheadint(0)
            my_turtle.penup()
            my_turtle.goto(r.c, r.y)
            my_turtle.pendown()
            my_turtle.forward(r.width)
            my_turtle.right(90)
            my_turtle.forward(r.height)
            my_turtle.right(90)
            my_turtle.forward(r.width)
            my_turtle.right(90)
            my_turtle.forward(r.height)
        for s in list_squares:
            my_turtle.setheadint(0)
            my_turtle.penup()
            my_turtle.goto(s.c, s.y)
            my_turtle.pendown()
            my_turtle.forward(s.size)
            my_turtle.right(90)
            my_turtle.forward(s.size)
            my_turtle.right(90)
            my_turtle.forward(s.size)
            my_turtle.right(90)
            my_turtle.forward(s.size)
        input()
