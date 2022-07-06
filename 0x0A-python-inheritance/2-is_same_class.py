#!/usr/bin/python3
"""function that returns True if the object
is exactly an instance of the specified class"""


def is_same_class(obj, a_class):
    """return True if obj is instance of a_class"""
    x = type(obj)
    if x == a_class:
        return True
    return False
