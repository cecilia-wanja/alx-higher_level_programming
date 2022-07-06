#!/usr/bin/python3
"""Module for BaseGeometry"""


class BaseGeometry:
    """BaseGeometry class"""

    def area(self):
        """Raises an Exception"""
        raise Exception("area() is not implemented")

    def integer_validator(self, name, value):
        """Validates value
        Raises:
            TypeError: If value is not an integer.
            ValueError: If value is <= 0.
        """
        if type(value) != int:
            raise TypeError(name + " must be an integer")
        if value <= 0:
            raise ValueError(name + " must be greater than 0")
