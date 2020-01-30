"""Contains code for StackADTs
CPE202
Project 1

Author:
    John Wright
"""
from array_list import ArrayList
import array_list
from linked_list import Node
import linked_list

class StackArray:
    """Stack using array list
    Attributes:
        arr_list (ArrayList) : An array
        num_items (int) : number of items
    """
    def __init__(self, num_items=0):
        self.arr_list = ArrayList()
        self.num_items = num_items

    def __repr__(self):
        pass

    def __eq__(self, other):
        if self.arr_list == other.arr_list and self.num_items == other.num_items:
            return True
        return False

    def is_empty(self):
        """Returns True if the Stack is empty.
        Args:
            self (StackArray): The stack we are checking the size of.
        Returns:
            (bool)
        """
        if self.num_items == 0:
            return True
        return False

    def push(self, item):
        """Push an item to the stack.
        Args:
            self (StackArray): The Stack
            item (): item to push to stack
        Returns
        """
        self.arr_list = array_list.insert(self.arr_list, item, self.num_items)
        self.num_items += 1

    def pop(self):
        """Pop an item from the stack
        Args:
            self (StackArray): The Stack
        Returns:
            (int): value popped from stack
        """
        val = 0
        if self.num_items == 0:
            raise IndexError('')
        self.arr_list, val = array_list.pop(self.arr_list, self.num_items - 1)
        self.num_items -= 1
        return val

    def peek(self):
        """returns the value at the top of the Stack.
        Args:
            self (StackArray): The Stack
        Returns:
            (int): Value at top of stack
        """
        if self.num_items == 0:
            raise IndexError('')
        return array_list.get(self.arr_list, self.num_items - 1)

    def size(self):
        """Returns the number of items in the Stack
        Args:
            self (StackArray): The Stack
        Returns:
            (int): Number of items in the stack
        """
        return self.num_items

class StackLinked:
    """Stack using linked list
    Attributes:
        top (Node) : a linked list
        num_items (int) : number of items
    """

    def __init__(self, top=None, num_items=0):
        self.top = top
        self.num_items = num_items

    def __repr__(self):
        pass

    def __eq__(self, other):
        pass

    def is_empty(self):
        """If stack is empty returns true else false.
        Args:
            self (StackLinked): Linked List Stack
        Returns:
            (bool): Whether list is empty
        """
        if self.top is None:
            return True
        return False

    def push(self, item):
        """Pushes item to the Stack
        Args:
            self (StackLinked): Linked List Stack
        """
        self.top = linked_list.insert(self.top, item, self.num_items)
        self.num_items += 1

    def pop(self):
        """Pop an item from the stack
        Args:
            self (StackArray): The Stack
        Returns:
            (int): int popped from stack
        """
        if self.top is None:
            raise IndexError('')
        self.top, item = linked_list.pop(self.top, self.num_items-1)
        self.num_items -= 1
        return item

    def peek(self):
        """Returns the value at the top of the Stack
        Args:
            self (StackArray): The Stack
        Returns:
            (int): value on top of stack
        """
        if self.top is None:
            raise IndexError('')
        return linked_list.get(self.top, self.num_items-1)

    def size(self):
        """Returns the number of items in the Stack
        Args:
            self (StackArray): The Stack
        Returns:
            (int): num of items in stack
        """
        return self.num_items
