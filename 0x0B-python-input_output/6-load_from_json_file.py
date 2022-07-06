#!/usr/bin/python3
"""Module that creates an Object from a JSON file"""


import json


def load_from_json_file(filename):
    """Creates an object from JSON file"""
    with open(filename, 'r') as open_file:
        return json.load(open_file)
