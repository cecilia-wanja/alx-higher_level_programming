#!/usr/bin/python3
"""
Defining a class Rectangle
"""


class Rectangle:
    """Rectangle class"""

    number_of_instances = 0
    print_symbol = "#"

    def __init__(self, width=0, height=0):
        """initializing the class"""
        self.__width = width
        self.__height = height
        Rectangle.number_of_instances += 1

    @property
    def width(self):
        """Retrieves width"""
        return self.__width

    @width.setter
    def width(self, widthValue):
        """Set width"""
        if type(widthValue) != int:
            raise TypeError("width must be an integer")
        if widthValue < 0:
            raise ValueError("width must be >= 0")
        self.__width = widthValue

    @property
    def height(self):
        """Retrieves the height"""
        return self.__height

    @height.setter
    def height(self, HeightValue):
        """Set height"""
        if type(HeightValue) != int:
            raise TypeError("height must be an integer")
        if HeightValue < 0:
            raise ValueError("height must be >= 0")
        self.__height = HeightValue

    def area(self):
        """Calculate area"""
        return self.__width * self.__height

    def perimeter(self):
        """Calculate perimeter"""
        width = self.__width
        height = self.__height
        if width == 0 or height == 0:
            return 0
        return (width + height) * 2

    def __str__(self):
        """Get string representation"""
        width = self.__width
        height = self.__height
        string = ""
        symbol = self.print_symbol
        if width == 0 or height == 0:
            return string
        for r in range(height):
            for c in range(width):
                string = string + str(symbol)
            string = string + '\n'
        return string[:-1]

    def __repr__(self):
        """Return the string representation of the Rectangle."""
        rect = "Rectangle(" + str(self.__width)
        rect += ", " + str(self.__height) + ")"
        return (rect)

    def __del__(self):
        """delete a rectangle"""
        Rectangle.number_of_instances -= 1
        print("Bye rectangle...")
