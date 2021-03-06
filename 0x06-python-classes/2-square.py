#!/usr/bin/python3
"""Module Sqaure"""

class Square:
    """Square class defined by geometric shap
       Attributes:
       size (int): Size of square
    """
    def __init__(self, size=0):
        """Initialize methode
        """
        if type(size) != int:
            raise TypeError("size must be an integer")
        elif size < 0:
            raise ValueError("size must be >= 0")                
        self.__size = size
