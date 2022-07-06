#!/usr/bin/python3
"""Module checks if object
is an instance of a class that inherited
(directly or indirectly) from the specified class"""


def inherits_from(obj, a_class):
    """Return if the object is an instance that inherited from the specified"""
    return isinstance(obj, a_class) and type(obj) != a_class
