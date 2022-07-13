#!/usr/bin/python3
"""
Module class Rectangle that inherits from Base
"""


from models.base import Base


class Rectangle(Base):
    """
    Rectangle - class that inherits from Base
    """
    def __init__(self, width, height, x=0, y=0, id=None):
        """
        Constructor for rectangle
        Arguments:
        @width: width of the rectangle
        @height: height of the rectangle
        @x: position in x
        @y: position in y
        @id: amount of instances created
        """
        self.width = width
        self.height = height
        self.x = x
        self.y = y
        super().__init__(id)

    @property
    def width(self):
        """ Getter for width """
        return self.__width

    @width.setter
    def width(self, value):
        """ Setter for width """
        if type(value) is not int:
            raise TypeError('width must be an integer')
        elif value <= 0:
            raise ValueError('width must be > 0')
        self.__width = value

    @property
    def height(self):
        """ Getter for height """
        return self.__height

    @height.setter
    def height(self, value):
        """ Setter for height """
        if type(value) is not int:
            raise TypeError('height must be an integer')
        elif value <= 0:
            raise ValueError('height must be > 0')
        self.__height = value

    @property
    def x(self):
        """ Getter for x """
        return self.__x

    @x.setter
    def x(self, value):
        """ Setter for x """
        self.validator("x", value)
        self.__x = value

    @property
    def y(self):
        """ Getter for y """
        return self.__y

    @y.setter
    def y(self, value):
        """ Setter for y """
        self.validator("y", value)
        self.__y = value

    # magic methods
    def __str__(self):
        """
        formats string representation of the Rectangle
        """
        return ("[{}] ({}) {}/{} - {}/{}".format(
                self.__class__.__name__, self.id,
                self.x, self.y, self.__width, self.__height))

    # public methods
    def validator(self, name, value):
        """
        validator - method that checks for legal values
        Arguments:
        @name: name of the attribute to check
        @value: value of the attribute to check
        Returns:
        A raise Type or Value error if is not an integer or
        if is not a positive number, respectly
        """
        if not isinstance(value, int):
            raise TypeError("{} must be an integer".format(name))
        if value < 0 and (name is "x" or name is "y"):
            raise ValueError("{} must be >= 0".format(name))

    def area(self):
        """
        area - method that returns the area value
        Returns:
        The area of the rectangle
        """
        return self.__width * self.__height

    def display(self):
        """
        display - method that prints in stdout the Rectangle instance
        with the character #
        """
        for posy in range(self.__y):
            print()
        for r in range(self.__height):
            for posx in range(self.__x):
                print(" ", end="")
            for c in range(self.__width):
                print('#', end="")
            print()

    def update(self, *args, **kwargs):
        """
        update - assign the arguments to each attribute
        @args: list of arguments
        @kargs: dictionary of arguments, key represents
        an attribute to the instance
        """
        for i in range(len(args)):
            if i == 0:
                self.id = args[0]
            elif i == 1:
                self.__width = args[1]
            elif i == 2:
                self.__height = args[2]
            elif i == 3:
                self.__x = args[3]
            elif i == 4:
                self.__y = args[4]
        if not args:
            for key, value in kwargs.items():
                if key == 'id':
                    self.id = value
                if key == 'width':
                    self.__width = value
                if key == 'height':
                    self.__height = value
                if key == 'x':
                    self.__x = value
                if key == 'y':
                    self.__y = value

    def to_dictionary(self):
        """
        to_dictionary - returns a dictionary representation of a Rectangle
        """
        temp = {}
        for key, value in self.__dict__.items():
            if key == 'id':
                temp[key] = value
            else:
                temp[key[12:]] = value
        return temp
