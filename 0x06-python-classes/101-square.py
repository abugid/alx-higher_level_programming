#!/usr/bin/python3
"""
This is the "Square"  module.
This module provides a simple Square class with initialize size.
Defaults size to 0. Raise error on invalid size inputs.
Attribute position which takes a default (0, 0) tuple.
Methods Getter and Setter properties for size and position.
Method area returns size of area of the square.
Method my_print prints the square using "#", moved over left and top using
position tuple.
Method __repr__ should return the string to print out the square.
"""


class Square:
    """A class that defines a square by size, which defaults 0.
    Also defines position using a tuple, which defaults (0, 0).
    Square can also get area, and print square using '#'.
    When printing, using position, offset on top and left.
    """
    def __init__(self, size=0, position=(0, 0)):
        self.size = size
        self.position = position

    @property
    def size(self):
        return self.__size

    @size.setter
    def size(self, value):
        if type(value) != int:
            raise TypeError("size must be an integer")
        elif value < 0:
            raise ValueError("size must be >= 0")
        else:
            self.__size = value

    @property
    def position(self):
        return self.__position

    @position.setter
    def position(self, value):
        if type(value) is tuple:
            if len(value) == 2:
                if not any(i < 0 for i in value):
                    self.__position = value
                    return
        raise TypeError("position must be a tuple of 2 positive integers")

    def area(self):
        return self.__size ** 2

    def my_print(self):
        if self.__size == 0:
            print()
        else:
            for i in range(self.__position[1]):
                print("")
            for i in range(self.__size):
                if self.__position[0]:
                    print(" " * self.__position[0], end="")
                print("#" * self.__size)

    def __str__(self):
        re_str = ""
        if self.__size != 0:
            for i in range(self.__position[1]):
                re_str += "\n"
            for i in range(self.__size):
                if self.__position[0]:
                    re_str += " " * self.__position[0]
                re_str += "#" * self.__size
                if i != self.__size - 1:
                    re_str += "\n"

        return re_str
