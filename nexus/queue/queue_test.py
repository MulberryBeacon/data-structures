# -*- coding: utf8 -*-

"""
Tests for the queue implementation.

Author: Eduardo Ferreira
License: MIT (see LICENSE for details)
"""

from nexus.queue.queue import Queue
import unittest

class QueueTests(unittest.TestCase):

    def setUp(self):
        self.queue = Queue()

    def tearDown(self):
        for x in range(self.queue.length()):
            self.queue.dequeue()

    def test_enqueue(self):
        size = self.queue.length()
        self.queue.enqueue(1)
        self.assertEqual(self.queue.length(), size + 1)

    def test_dequeue(self):
        self.queue.enqueue(1)
        size = self.queue.length()
        first = self.queue.dequeue()
        self.assertEqual(first, 1)
        self.assertEqual(self.queue.length(), size - 1)

    def test_pop_empty(self):
        first = self.queue.dequeue()
        self.assertEqual(first, None)

    def test_not_empty(self):
        self.queue.enqueue(1)
        self.assertEqual(self.queue.empty(), False)

    def test_empty(self):
        self.assertEqual(self.queue.empty(), True)

if __name__ == '__main__':
    unittest.main()
