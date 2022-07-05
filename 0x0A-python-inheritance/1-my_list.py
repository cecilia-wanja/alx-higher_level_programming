#!/usr/bin/python3
"""Class that inherits from list"""


class MyList(list):
    """MyList class"""

    def print_sorted(self):
        """Print the sorted list"""
        print(sorted(self))
