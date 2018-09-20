# -*- coding: utf8 -*-

"""
Simple implementation of a binary search tree.

Author: Eduardo Ferreira
License: MIT (see LICENSE for details)
"""

class Node():
    def __init__(self, data):
        self.data = data
        self.left = None
        self.right = None


    def insert(self, value):
        if value <= self.data:
            if self.left == None:
                self.left = Node(value)
            else:
                self.left.insert(value)
        else:
            if self.right == None:
                self.right = Node(value)
            else:
                self.right.insert(value)


    def contains(self, value) -> bool:
        if value == self.data:
            return True
        elif value < self.data:
            if self.left == None:
                return False
            else:
                return self.left.contains(value)
        else:
            if self.right == None:
                return False
            else:
                return self.right.contains(value)


    def traverseInOrder(self):
        if self.left != None:
            self.left.traverseInOrder()

        print(self.data)

        if self.right != None:
            self.right.traverseInOrder()


    def traversePreOrder(self):
        print(self.data)

        if self.left != None:
            self.left.traversePreOrder()

        if self.right != None:
            self.right.traversePreOrder()


    def traversePostOrder(self):
        if self.left != None:
            self.left.traversePostOrder()

        if self.right != None:
            self.right.traversePostOrder()

        print(self.data)


    def length(self) -> int:
        size = 1
        if self.left != None:
            size += self.left.length()

        if self.right != None:
            size += self.right.length()

        return size
