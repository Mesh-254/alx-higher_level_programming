#!/usr/bin/python3
"""
a function to check if the object is instance of class
"""
def is_kind_of_class(obj, a_class):
    """
    function that returns True if the object is an instance of
     or if the object is an instance of a class that inherited from,
    """
    if isinstance(obj, a_class):
        return True 
    return False
