# -*- coding: utf8 -*-

"""
Simple implementation of a stack (LIFO).

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
    def __init__(self):
        self.stack = []
        self.top = 0

    def __repr__(self):
        return 'Stack(%s)' % self.stack

    def push(self, element):
        self.stack.insert(self.top, element)

    def pop(self):
        if (self.empty()):
            return None

        element = self.stack[self.top]
        del self.stack[self.top]
        return element

    def peek(self):
        return self.stack[self.top]

    def empty(self):
        return len(self.stack) == 0

    def length(self):
        return len(self.stack)
