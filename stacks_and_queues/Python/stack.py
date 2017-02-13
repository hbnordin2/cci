import copy


class Stack:
    """
    This stack is made using Python's dynamic array data structure. On initialization, this stack is empty. Only
    copies of elements are returned from this class. Elements can be pushed onto this stack using either stack + element
    or by using the push method defined.
    """
    def __init__(self):
        self.__stack = []

    def pop(self):
        """
        Returns and removes the element that was last pushed onto the stack
        :return: The element most recently pushed onto the stack
        """
        return self.__stack.pop()

    def push(self, element):
        """
        Adds an element to the top of a stack
        :param element: The item to add to the top of the stack
        """
        self.__stack.append(element)

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

    def __add__(self, element):
        """
        Pushes an element onto the top of this stack
        :param element: The element to push onto the top of this stack
        """
        self.push(element)

    def __str__(self):
        """
        Returns a list representation of the stack, where the rightmost element is at the top of the stack
        :return: A list representation of the stack, where the rightmost element is at the top of the stack
        """
        return str(self.stack)

    @property
    def stack(self):
        return copy.deepcopy(self.__stack)