# -*- coding: utf8 -*-

"""
Simple representation of a stack with push and pop operations.

Essential operations:
* push :: adds an element to the top of the stack
* pop  :: removes the element at the top of the stack (the most recently added element that hasn't been removed)

Non-essential operations:
* peek   :: returns the element at the top of the stack without changing the stack
* empty  :: checks if the stack is empty
* length :: returns the number of elements in the stack (useful for testing)

Author: Eduardo Ferreira
License: MIT (see LICENSE for details)
"""

class Stack():
    def __init__(self, stack=[]):
        self.stack = stack

    def __repr__(self):
        return 'Stack(%s)' % self.stack

    def push(self, element):
        self.stack.insert(0, element)

    def pop(self):
        if (self.empty()):
            return None

        element = self.stack[0]
        del self.stack[0]
        return element

    def peek(self):
        return self.stack[0]

    def empty(self):
        return len(self.stack) == 0

    def length(self):
        return len(self.stack)
