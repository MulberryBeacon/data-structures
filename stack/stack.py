# -*- coding: utf8 -*-

"""
Simple representation of a stack with push and pop operations.

Author: Eduardo Ferreira
License: MIT (see LICENSE for details)
"""

class Stack():
    def __init__(self, stack=[]):
        self.stack = stack

    def __push__(self, element):
        self.stack.insert(0, element)

    def __pop__(self):
        element = self.stack[0]
        del self.stack[0]
        return element
