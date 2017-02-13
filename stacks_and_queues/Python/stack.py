import copy


class Stack:
    """
    An implementation of a stack
    """
    def __init__(self):
        """
        Stack initializes as an empty stack.
        """
        self.__stack = []

    def pop(self):
        """
        Returns and removes the element that was last pushed onto the stack
        :return: The element most recently pushed onto the stack
        """
        return self.__stack.pop()

    def push(self, item):
        """
        Adds an element to the top of a stack
        :param item: The item to add to the top of the stack
        """
        self.__stack.append(item)

    def is_empty(self):
        """
        Returns true if and only if the stack is empty
        :return: True if and only if the stack if empty
        """
        if len(self.__stack) == 0:
            return True
        return False

    def peek(self):
        """
        Returns the element that was last pushed onto the stack
        :return: The element that was last pushed onto the stack
        """
        return copy.deepcopy(self.__stack[-1])

    @property
    def stack(self):
        return copy.deepcopy(self.__stack)