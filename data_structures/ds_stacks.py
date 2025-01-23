"""
Stack
A stack is a LIFO (Last In, First Out) data structure. The last element added to the stack is the first one to be removed.
You can implement a stack using a list in Python.

Key Operations:
Push: Add an element to the stack.
Pop: Remove and return the top element from the stack.
Peek: View the top element without removing it.
is_empty: Check if the stack is empty.
"""


class Stack:
    def __init__(self):
        self.stack = []

    def push(self, item):
        self.stack.append(item)

    def pop(self):
        if not self.is_empty():
            return self.stack.pop()
        return None

    def peek(self):
        if not self.is_empty():
            return self.stack[-1]
        return None

    def is_empty(self):
        return len(self.stack) == 0


# Testing the Stack class
s = Stack()
s.push(1)
s.push(2)
s.push(3)
print(s.peek())
print(s.pop())
print(s.pop())
