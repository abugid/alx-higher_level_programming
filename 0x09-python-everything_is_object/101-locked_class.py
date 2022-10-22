#!/usr/bin/python3
"""
    This is a module to create a locked class
"""


class LockedClass:
    """
        this locked class will not have any class or object atributes
        and any dynamic creation of an instance attribute will be rejected
        if it does not have the name first_name
    """
    __slots__ = ['first_name']
