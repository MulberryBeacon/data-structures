# -*- coding: utf8 -*-

"""
Tests for the queue implementation.

Author: Eduardo Ferreira
License: MIT (see LICENSE for details)
"""

from nexus.linked_list.linked_list import LinkedList
import unittest

class LinkedListTests(unittest.TestCase):

    def setUp(self):
        self.linked_list = LinkedList()

    def tearDown(self):
        self.linked_list.head = None

    def test_append(self):
        size = self.linked_list.length()
        self.linked_list.append(1)
        self.assertEqual(self.linked_list.length(), size + 1)

    def test_prepend(self):
        self.linked_list.append(1)
        self.linked_list.append(2)
        size = self.linked_list.length()
        head = self.linked_list.head
        self.linked_list.prepend(3)
        self.assertEqual(self.linked_list.length(), size + 1)
        self.assertEqual(self.linked_list.head.next.data, head.data)

    def test_get_with_value(self):
        self.linked_list.append(1)
        self.linked_list.append(2)
        self.linked_list.append(3)
        value = self.linked_list.get_with_value(2)
        self.assertEqual(value, 2)

    def test_delete_with_value(self):
        self.linked_list.append(1)
        self.linked_list.append(2)
        self.linked_list.append(3)
        size = self.linked_list.length()
        self.linked_list.delete_with_value(2)
        self.assertEqual(self.linked_list.length(), size - 1)
        self.assertIsNone(self.linked_list.get_with_value(2))

    def test_delete_with_value_head(self):
        self.linked_list.append(1)
        self.linked_list.append(2)
        self.linked_list.append(3)
        size = self.linked_list.length()
        head = self.linked_list.head
        self.linked_list.delete_with_value(1)
        self.assertIsNot(self.linked_list.head.data, head.data)
        self.assertEqual(self.linked_list.length(), size - 1)
        self.assertIsNone(self.linked_list.get_with_value(1))

    def test_not_empty(self):
        self.linked_list.append(1)
        self.assertFalse(self.linked_list.empty())

    def test_empty(self):
        self.assertTrue(self.linked_list.empty())

if __name__ == '__main__':
    unittest.main()
