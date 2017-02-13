from unittest import TestCase
from .stack import Stack


class TestStack(TestCase):
    def test_push(self):
        stack = Stack()
        stack.push(1)
        stack.push("cat")
        stack.push(True)
        self.assertEquals(stack.stack, [1, "cat", True], "Stack push is incorrect")

    def test_peek(self):
        stack = Stack()
        stack.push(1)
        self.assertEquals(stack.peek(), 1)
        self.assertEquals(stack.stack, [1])
        stack.push(2)
        self.assertEquals(stack.peek(), 2)
        self.assertEquals(stack.stack, [1, 2])

    def test_immutability(self):
        stack = Stack()
        stack.push("hello")
        stack_copy = stack.stack
        stack_copy.pop()
        self.assertEquals(stack.stack, ["hello"])

    def test_is_empty(self):
        stack = Stack()
        self.assertEquals(stack.is_empty(), True)
        stack.push(1)
        self.assertEquals(stack.is_empty(), False)
        stack.pop()
        self.assertEquals(stack.is_empty(), True)

    def test_pop(self):
        stack = Stack()
        stack.push(1)
        stack.push("hello")
        self.assertEquals(stack.pop(), "hello")
        self.assertEquals(stack.pop(), 1)

    def test_peek_immutability(self):
        stack = Stack()
        stack.push([1])
        list_element = stack.peek()
        list_element.append(2)
        self.assertEquals(stack.stack, [[1]])

    def test_add_sign(self):
        stack = Stack()
        stack + 1
        stack + 2
        self.assertEquals(stack.stack, [1, 2])
