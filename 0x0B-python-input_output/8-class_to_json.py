#!/usr/bin/python3
"""class_to_json module
returns the dictionary description with simple data structure
for JSON serialization of an object
"""


def class_to_json(obj):
    """Returns dictionary description with data list"""
    return obj.__dict__
