#!/usr/bin/python3
"""
 class Rectangle that inherits from Base
"""
from models import Base


class Rectangle(Base):
    """initialize the representation class rectangle"""

    def __init__(self, width, height, x=0, y=0, id=None):
        """ initialize the representation class rectangle """
        self.__width = width
        self.__height = height
        self.__x = x
        self.__y = y 
        super().__init__(id)
    
    @property
    def width(self, value):
        """width getter"""
        return self.__width

    @width.setter
    def width(self, value):
        """width setter"""
        if type(value) != int:
            raise TypeError ('width must be an integer')
        if value <= 0:
            raise ValueError("width must be > 0")
        self.__width = value

    @property
    def height(self):
        """ the getter of height"""
        return self.__height

    @height.setter
    def height(self, value):
        """the setter of height"""
        if type(value) != int:
            raise TypeError('height must be an integer')
        if value <= 0:
            raise ValueError("height must be > 0")
        self.__height = value

    @property
    def x(self):
        """ the getter of x"""
        return self.__x

    @x.setter
    def x(self, value):
        """the setter of x"""
        if type(value) != int:
            raise TypeError('x must be an integer')
        if value < 0:
            raise ValueError("x must be >= 0")
        self.__x = value

    @property
    def y(self):
        """the getter of y"""
        return self.__y

    @y.setter
    def y(self, value):
        """ y setter"""
        if type(value) != int:
            raise TypeError('y must be an integer')
        if value < 0:
            raise ValueError("y must be >= 0")
        self.__y = value

    def area(self):
        """returns the area value of the Rectangle"""
        return self.__width * self.__height

    def display(self):
        """Display The Rectangle Using  '#'"""
        for k in range(self.__y):
            print()
        for i in range(self.__height):
            print(" " * self.__x, end="")
            for j in range(self.__width):
                print("#", end="")
            print()

    def __str__(self):
        """ return the string representation of the Rectangle"""
        return "{} ({}) {}/{} - {}/{}".format(self.__class__.__name__, self.id, self.__x, self.__y, self.__width, self.__height)

    def update(self, *args, **kwargs):
        """ update the rectangle with keyword and non keyword arguments."""
        if len(kwargs) != 0:
            for k, v in kwargs.items():
                setattr(self, k, v)
        elif len(args) != 0:
            try:
                self.id = args[0]
                self.__width = args[1]
                self.__height = args[2]
                self.__x = args[3]
                self.__y = args[4]
            except IndexError:
                pass

    def to_dictionary(self):
        """ return dictionary representation of rectangle"""
        return self.__dict__
        

