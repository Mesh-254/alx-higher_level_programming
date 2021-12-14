#!/usr/bin/python3
"""
Locked Class Module

"""
class LockedClass:
    """prevents the user from dynamically creating new inst    """
    __slots__ = 'first_name'
