# -*- coding: utf8 -*-

"""
Simple implementation of a linked list.

Essential operations:
* enqueue :: adds an element to the end of the queue
* dequeue :: removes the element at the beginning of the queue

Non-essential operations:
* empty  :: checks if the linked list is empty
* length :: returns the number of elements in the queue (useful for testing)

Operation | Average | Worst case
----------|---------|-----------
Search    | O(n)    | O(n)
Append    | O(n)    | O(n)
Prepend   | O(1)    | O(1)
Delete    | O(n)    | O(n)

Author: Eduardo Ferreira
License: MIT (see LICENSE for details)
"""

class Node():
    def __init__(self, data):
        self.data = data
        self.next = None


class LinkedList():
    def __init__(self):
        self.head = None


    def append(self, data):
        if self.head == None:
            self.head = Node(data)
            return

        current = self.head
        while current.next != None:
            current = current.next

        current.next = Node(data)


    def prepend(self, data):
        newHead = Node(data)
        newHead.next = self.head
        self.head = newHead


    def get_with_value(self, data):
        if self.head == None:
            return None

        if self.head.data == data:
            return self.head.data

        current = self.head
        while current.next != None:
            if current.next.data == data:
                return current.next.data

            current = current.next


    def delete_with_value(self, data):
        if self.head == None:
            return None

        if self.head.data == data:
            self.head = self.head.next
            return None

        current = self.head
        while current.next != None:
            if current.next.data == data:
                current.next = current.next.next
                return None

            current = current.next


    def empty(self) -> bool:
        return self.head == None


    def length(self) -> int:
        if self.head == None:
            return 0

        size = 1
        current = self.head
        while current.next != None:
            current = current.next
            size += 1

        return size
