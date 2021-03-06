#!/usr/bin/python3

"""

This is the "Rectangle"  module.

This module provides a simple Rectangle class.

"""
class Rectangle:
    """A simple Rectangle class"""
    def __init__(self, width=0, height=0):
        """ a rectangle initializes a rectangle"""
        self.width = width
        lf.height = height
    
    @property
    def width(self):
        """ width of the rectangle getter"""
        return self.__width
    @width.setter
    def width(self, value):
        """ width of rectangle setter"""
        if type(value) is not int:
            raise TypeError("width must be an integer")
        if value < 0:
            raise ValueError("width must be >= 0")
        elf.__width = value
    @property
    def height(self):
        """ height of rectangle getter"""
        return self.__height

    @height.setter
    def height(self, value):
        """ height of rectangle setter"""
        if type(value) is not int:
            raise TypeError("height must be an integer")
         if value < 0:
            raise ValueError("height must be >= 0")
        self.__height = value
