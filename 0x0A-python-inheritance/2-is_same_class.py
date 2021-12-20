#!/usr/bin/python3
"""
This module contains the function is_same_class
"""
def is_same_class(obj, a_class):
    """
    check instance and class return true if obj is the exact class a_class, else false"""
    return type(obj) == a_class
