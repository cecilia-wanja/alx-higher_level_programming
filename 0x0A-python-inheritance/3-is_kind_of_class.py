#!/usr/bin/python3
"""Module that checks if an object is an instance
of a class inherited from"""


def is_kind_of_class(obj, a_class):
    """return True if obj is instance of a_class"""
    return isinstance(obj, a_class)
