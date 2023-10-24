#!/usr/bin/python3

"""This module defines classes for a singly-linked list."""


class ListNode:
    """This class represents a node in a singly-linked list."""

    def __init__(self, data, next_node=None):
        """Initialize a new ListNode.

        Args:
            data (int): The data stored in the new ListNode.
            next_node (ListNode): The next node in the list after this one.
        """
        self.data = data
        self.next_node = next_node

    @property
    def data(self):
        """Get or set the data stored in the ListNode."""
        return (self.__data)

    @data.setter
    def data(self, value):
        if not isinstance(value, int):
            raise TypeError("Data must be an integer")
        self.__data = value

    @property
    def next_node(self):
        """Get or set the next node in the list after this one."""
        return (self.__next_node)

    @next_node.setter
    def next_node(self, value):
        if not isinstance(value, ListNode) and value is not None:
            raise TypeError("Next node must be a ListNode object")
        self.__next_node = value


class SinglyLinkedList:
    """This class represents a singly-linked list."""

    def __init__(self):
        """Initialize a new SinglyLinkedList."""
        self.__head = None

    def sorted_insert(self, value):
        """Insert a new ListNode into the SinglyLinkedList.

        The node is inserted into the list at the correct
        ordered numerical position.

        Args:
            value (ListNode): The new ListNode to insert.
        """
        new_node = ListNode(value)
        if self.__head is None:
            new_node.next_node = None
            self.__head = new_node
        elif self.__head.data > value:
            new_node.next_node = self.__head
            self.__head = new_node
        else:
            current_node = self.__head
            while (current_node.next_node is not None and
                    current_node.next_node.data < value):
                current_node = current_node.next_node
            new_node.next_node = current_node.next_node
            current_node.next_node = new_node

    def __str__(self):
        """Define the print() representation of a SinglyLinkedList."""
        node_values = []
        current_node = self.__head
        while current_node is not None:
            node_values.append(str(current_node.data))
            current_node = current_node.next_node
        return ('\n'.join(node_values))
