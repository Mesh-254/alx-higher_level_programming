#!/usr/bin/python3
"""
returns sorted list
"""
class MyList(list):
    """
    returns sorted list
    """
    def __init__ (self):
        """initialize class """
        super().__init__()
    def print_sorted(self):
        """"
        prints sorted list
        """
        print(sorted(self))
