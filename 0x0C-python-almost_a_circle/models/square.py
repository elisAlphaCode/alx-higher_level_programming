#!/usr/bin/python3
"""
Module class Square that inherits from Rectangle
"""


from models.rectangle import Rectangle


class Square(Rectangle):
    """
    Square - class for a square, this class inherit form Rectangle
    """
    def __init__(self, size, x=0, y=0, id=None):
        """
        Constructor for square
        Arguments:
        @size: size of the rectangle
        @x: position in x
        @y: position in y
        @id: amount of instances created
        """
        super().__init__(size, size, x, y, id)

    @property
    def size(self):
        """ Getter for width of square """
        return self.width

    @size.setter
    def size(self, value):
        """ Setter for size of square """
        if type(value) is not int:
            raise TypeError('width must be an integer')
        elif value <= 0:
            raise ValueError('width must be > 0')
        self.width = value
        self.height = value

    # magic methods

    def __str__(self):
        """
        formats string representation of the Square
        """
        return ("[{}] ({}) {}/{} - {}".format(
                self.__class__.__name__, self.id,
                self.x, self.y, self.width))

    # public methods

    def update(self, *args, **kwargs):
        """
        update - assign the arguments to each attribute
        @args: list of arguments
        @kargs: dictionary of arguments, key represents
        an attribute to the instance
        """
        if len(args) > 0:
            if args[0] is not None:
                self.id = args[0]
            if len(args) > 1:
                self.width = args[1]
                self.height = args[1]
            if len(args) > 2:
                self.x = args[2]
            if len(args) > 3:
                self.y = args[3]
        if not args:
            for key, value in kwargs.items():
                if key == 'id':
                    self.id = value
                if key == "size":
                    self.width = value
                    self.height = value

                if key == 'x':
                    self.x = value
                if key == 'y':
                    self.y = value

    def to_dictionary(self):
        """
        to_dictionary - returns a dictionary representation of a Square
        """
        return {'x': self.x, 'y': self.y, 'id': self.id, 'size': self.width}
