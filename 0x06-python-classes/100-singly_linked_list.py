#!/usr/bin/python3
"""
This is the "Single Linked List" module.
Class Node takes in integer values as data within each node,
and a next attribute which points to the next node or to None.
Class SinglyLinkedList initializes a default head of None.
Method sorted_insert handles all nodes created and adds them to
the linked list sorted by the int value stored within.
"""


class Node:
    """A class that creates a single Node in a Linked List.
    """
    def __init__(self, data, next_node=None):
        self.data = data
        self.next_node = next_node

    @property
    def data(self):
        return self.__data

    @data.setter
    def data(self, value):
        if type(value) is int:
            self.__data = value
        else:
            raise TypeError("data must be an integer")

    @property
    def next_node(self):
        return self.__next_node

    @next_node.setter
    def next_node(self, value):
        if (value is not None) and type(value) is not Node:
            raise TypeError("next_node must be a Node object")
        else:
            self.__next_node = value


class SinglyLinkedList:
    """A class that creates a Singly Linked List.
    """
    def __init__(self):
        self.__head = None

    def sorted_insert(self, value):
        if self.__head is None:
            self.__head = Node(value)
        else:
            tmp = self.__head
            tmp2 = tmp.next_node
            if self.__head.data > value:
                new_node = Node(value, self.__head)
                self.__head = new_node
                return
            while (tmp2):
                if tmp2.data > value:
                    tmp.next_node = Node(value, tmp2)
                    break
                tmp = tmp2
                tmp2 = tmp2.next_node
            else:
                tmp.next_node = Node(value)

    def __str__(self):
        re_str = ""
        tmp = self.__head
        while (tmp):
            re_str += str(tmp.data)
            tmp = tmp.next_node
            if (tmp):
                re_str += "\n"
        return re_str
