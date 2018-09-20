# -*- coding: utf8 -*-

"""
Tests for the binary search tree implementation.

Author: Eduardo Ferreira
License: MIT (see LICENSE for details)
"""

from nexus.tree.tree import Node
import unittest

class TreeTests(unittest.TestCase):

    def setUp(self):
        self.tree = Node(5)
        self.tree.insert(1)
        self.tree.insert(2)
        self.tree.insert(8)
        self.tree.insert(6)
        self.tree.insert(10)

    def test_insert(self):
        size = self.tree.length()
        self.tree.insert(7)
        self.assertEqual(self.tree.length(), size + 1)

    def test_contains_true(self):
        self.assertTrue(self.tree.contains(6))

    def test_contains_false(self):
        self.assertFalse(self.tree.contains(11))

if __name__ == '__main__':
    unittest.main()
