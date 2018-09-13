# -*- coding: utf8 -*-

"""
Simple implementation of a queue (FIFO).

Essential operations:
* enqueue :: adds an element to the end of the queue
* dequeue :: removes the element at the beginning of the queue

Non-essential operations:
* empty  :: checks if the queue is empty
* length :: returns the number of elements in the queue (useful for testing)

Operation | Average | Worst case
----------|---------|-----------
Space     | O(n)    | O(n)
Search    | O(n)    | O(n)
Insert    | O(1)    | O(1)
Delete    | O(1)    | O(1)

Author: Eduardo Ferreira
License: MIT (see LICENSE for details)
"""

class Queue():
    def __init__(self, queue=[]):
        self.queue = queue

    def __repr__(self):
        return 'Queue(%s)' % self.queue

    def enqueue(self, element):
        self.queue.append(element)

    def dequeue(self):
        if (self.empty()):
            return None

        element = self.queue[0]
        del self.queue[0]
        return element

    def empty(self):
        return len(self.queue) == 0

    def length(self):
        return len(self.queue)
