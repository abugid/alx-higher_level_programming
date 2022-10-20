#!/usr/bin/python3
"""
This is the "Rectangle"  module.
This module provides a Rectangle class.
"""


class Rectangle:
    """A Rectangle class with attributes width and height,
    methods area, perimeter, print, str, repr, and del, and
    class attribute number_of_instances that keeps track of # of instances,
    and class attribute print_symbol which is used as symbol for printing.
    """

    number_of_instances = 0
    print_symbol = "#"

    def __init__(self, width=0, height=0):
        self.height = height
        self.width = width
        Rectangle.number_of_instances += 1
        type(self).print_symbol = "#"

    @property
    def width(self):
        return self.__width

    @width.setter
    def width(self, value):
        if type(value) is not int:
            raise TypeError("width must be an integer")
        elif value < 0:
            raise ValueError("width must be >= 0")
        self.__width = value

    @property
    def height(self):
        return self.__height

    @height.setter
    def height(self, value):
        if type(value) is not int:
            raise TypeError("height must be an integer")
        elif value < 0:
            raise ValueError("height must be >= 0")
        self.__height = value

    @property
    def print_symbol(self):
        return type(self).print_symbol

    @print_symbol.setter
    def print_symbol(self, value):
        type(self).print_symbol = value

    def area(self):
        return self.width * self.height

    def perimeter(self):
        if self.width == 0 or self.height == 0:
            return 0
        return 2 * (self.width + self.height)

    def __str__(self):
        if self.width == 0 or self.height == 0:
            return ""
        re_str = ""
        for i in range(self.height):
            re_str += str(self.print_symbol) * self.width
            if i != self.height - 1:
                re_str += "\n"
        return re_str

    def __repr__(self):
        return f"Rectangle({self.width}, {self.height})"

    def __del__(self):
        Rectangle.number_of_instances -= 1
        print("Bye rectangle...")
