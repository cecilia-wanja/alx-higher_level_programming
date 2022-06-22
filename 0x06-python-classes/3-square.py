#!/usr/bin/python3
'''Defines a class Square'''


class Square:
    '''Defines a class Square'''

    def __init__(self, size=0):
        '''Constructor. Initializes a new square.


        Args:
            size: The size of the new square.


        Raises:
            TypeError: if size is not an integer.
            ValueError: If size < 0.
        '''
        if not isinstance(size, int):
            raise TypeError("size must be an integer")
        elif size < 0:
            raise ValueError("size must be >= 0")
        self.__size = size

    def area(self):
        '''Returns the current area of the square.'''
        return (self.__size * self.__size)
