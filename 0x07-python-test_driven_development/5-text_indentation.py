#!/usr/bin/python3
"""
This is a module to print out indeted text
it takes in a string and prints on every new line
string separated by ?, . or :
"""


def text_indentation(text):
    """this a function that prints a string with the proper formatting
    if the argument passed is not a string it raises a typeerror
    otherwise it prints a string separated by predefined speparators
    on a new line
    """
    if type(text) is not str:
        raise TypeError("text must be a string")
    line = ""
    for i in text:
        line += i
        if i in ["?", ".", ":"]:
            print(f"{line.strip()}\n")
            line = ""

    print(line.strip(), end="")
