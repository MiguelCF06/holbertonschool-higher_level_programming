#!/usr/bin/python3
"""Write a Node class for a singly linked list"""


class Node:
    """Represents a node in a singly linked list

    Attributes:
        __data (int): data stored inside the node
        __next_node (Node): next node in the linked list
    """
    def __init__(self, data, next_node=None):
        """Initializes the node

        Arguments:
            data (int): data stored inside the node
            next_node (Node): next node in the linked list

        Returns: None
        """
        self.data = data
        self.next_node = next_node


    @property
    def data(self):
        """getter of __data

        Returns: data stored inside the node
        """
        return self.__data

    @data.setter
    def data(self, value):
        """setter of __data

        Arguments:
              value (int): data stored insite the node

        Returns: None
        """
        if type(value) is int:
            self.__data = value
        else:
            raise TypeError("data must be an integer")

    @property
    def next_node(self):
        """getter of __next_node

        Returns: the next node in the linked list
        """
        return self.__next_node


    @next_node.setter
    def next_node(self, value):
        """setter of __next_node

        Arguments:
            value (Node): next node in the linked list

        Returns: None
        """
        if value is None or isinstance(value, Node):
            self.__next_node = value
        else:
            raise TypeError("next_node must be a Node object")

    def __str__(self):
        """String representation of Node instance

        Returns: Formatted string representing the node
        """
        return str(self.__data)

class SinglyLinkedList:
    """Represents a single linked list

    Attributes:
         __head (Node): head of the linked list
    """
    def __init__(self):
        """Initializes the linked list

        Returns: None
        """
        self.__head = None

    def sorted_insert(self, value):
        """inserts a new Node instance into the correct sorted position

        Arguments:
            value (int): data stored inside the new node

        Returns: None
        """
        new_node = Node(value)
        temporal = self.__head
        if temporal is None or temporal.data >= value:
            if temporal:
                new_node.next_node = temporal
            self.__head = new_node
            return
        while temporal.next_node is not None:
            if temporal.next_node.data >= value:
                break
            temporal = temporal.next_node
        new_node.next_node = temporal.next_node
        temporal.next_node = new_node

    def __str__(self):
        """String representation of SinglyLinkedList instance

        Returns: Formatted string representing the linked list
        """
        string = ""
        temporal = self.__head
        while temporal is not None:
            string += str(temporal)
            if temporal.next_node is not None:
                string += "\n"
            temporal = temporal.next_node
        return string
