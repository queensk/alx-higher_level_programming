#!/usr/bin/python3
""" Create node
"""


class Node:
    """ Node init with data and next node
    """

    def __init__(self, data, next_node=None):
        """
                Instantiation with data and node
        Args:
            data: size of the square
            next_node: next node
        """
        self.data = data
        self.next_node = next_node

    @property
    def data(self):
        """
        Returns the privet data
        """
        return self.__data

    @data.setter
    def data(self, value):
        """
                Instantiation with data value
        Args:
            value: data value
        """
        if not isinstance(value, int):
            raise TypeError("data must be an integer")
        self.__data = value

    @property
    def next_node(self):
        """
        Returns the next node
        """
        return self.__next_node

    @next_node.setter
    def next_node(self, value):
        """
                Instantiation with value
        Args:
            value: data value of next node
        """
        if not isinstance(value, Node) and value is not None:
            raise TypeError("next_node must be a Node object")
        self.__next_node = value


"""
creares an empyt singlylikedlist
"""


class SinglyLinkedList:
    """
    Empyt sigle linked list.
    """

    def __str__(self):
        """
        Returns the vlaue of the singlylinked list
        """
        rtn = ""
        ptr = self.__head

        while ptr is not None:
            rtn += str(ptr.data)
            if ptr.next_node is not None:
                rtn += "\n"
            ptr = ptr.next_node

        return rtn

    def __init__(self):
        """
        instantiati head to None
        """
        self.__head = None

    def sorted_insert(self, value):
        """
                Sort Inserted data
        Args:
            value: data to be insarted
        """
        ptr = self.__head

        while ptr is not None:
            if ptr.data > value:
                break
            ptr_prev = ptr
            ptr = ptr.next_node

        newNode = Node(value, ptr)
        if ptr == self.__head:
            self.__head = newNode
        else:
            ptr_prev.next_node = newNode
