class Node:
    """This class represents a node in a singly-linked list."""

    def __init__(self, data, next_node=None):
        """Initialize a new Node.

        Args:
            data (int): The data stored in the new Node.
            next_node (Node): The next node in the list after this one.
        """
        self.data = data
        self.next_node = next_node

    @property
    def data(self):
        """Get or set the data stored in the Node."""
        return self.__data

    @data.setter
    def data(self, value):
        if not isinstance(value, int):
            raise TypeError("data must be an integer")
        self.__data = value

    @property
    def next_node(self):
        """Get or set the next node in the list after this one."""
        return self.__next_node

    @next_node.setter
    def next_node(self, value):
        if value is not None and not isinstance(value, Node):
            raise TypeError("next_node must be a Node object")
        self.__next_node = value


class SinglyLinkedList:
    """This class represents a singly-linked list."""

    def __init__(self):
        """Initialize a new SinglyLinkedList."""
        self.__head = None

    def __str__(self):
        """Define the print() representation of a SinglyLinkedList."""
        node_values = []
        current_node = self.__head
        while current_node is not None:
            node_values.append(str(current_node.data))
            current_node = current_node.next_node
        return '\n'.join(node_values)

    def sorted_insert(self, value):
        """Insert a new Node into the SinglyLinkedList.

        The node is inserted into the list at the correct
        ordered numerical position.

        Args:
            value (int): The new Node's data to insert.
        """
        new_node = Node(value)
        if self.__head is None or value < self.__head.data:
            new_node.next_node = self.__head
            self.__head = new_node
        else:
            current_node = self.__head
            while (current_node.next_node is not None and
                    current_node.next_node.data < value):
                current_node = current_node.next_node
            new_node.next_node = current_node.next_node
            current_node.next_node = new_node
