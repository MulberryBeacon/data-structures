# -*- coding: utf8 -*-

"""
Tests for the stack implementation.

Author: Eduardo Ferreira
License: MIT (see LICENSE for details)
"""

# Module import
# --------------------------------------------------------------------------------------------------
from nexus.stack.stack import Stack
import unittest


# Test class
# --------------------------------------------------------------------------------------------------
class StackTests(unittest.TestCase):

    def setUp(self):
        self.stack = Stack()

    def tearDown(self):
        for x in range(self.stack.length()):
            self.stack.pop()

    def test_push(self):
        size = self.stack.length()
        self.stack.push(1)
        self.assertEqual(self.stack.length(), size + 1)

    def test_pop(self):
        self.stack.push(1)
        size = self.stack.length()
        top = self.stack.pop()
        self.assertEqual(top, 1)
        self.assertEqual(self.stack.length(), size - 1)

    def test_pop_empty(self):
        top = self.stack.pop()
        self.assertEqual(top, None)

    def test_peek(self):
        self.stack.push(1)
        self.stack.push(2)
        top = self.stack.peek()
        self.assertEqual(top, 2)

    def test_not_empty(self):
        self.stack.push(1)
        self.assertEqual(self.stack.empty(), False)

    def test_empty(self):
        self.assertEqual(self.stack.empty(), True)


# Methods :: Execution and boilerplate
# --------------------------------------------------------------------------------------------------
if __name__ == '__main__':
    unittest.main()
