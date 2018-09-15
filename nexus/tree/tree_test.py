# -*- coding: utf8 -*-

"""
Tests for the tree implementation.

Author: Eduardo Ferreira
License: MIT (see LICENSE for details)
"""

# Module import
# --------------------------------------------------------------------------------------------------
from nexus.tree.tree import Tree
import unittest


# Test class
# --------------------------------------------------------------------------------------------------
class TreeTests(unittest.TestCase):

    def setUp(self):
        self.tree = Tree()


# Methods :: Execution and boilerplate
# --------------------------------------------------------------------------------------------------
if __name__ == '__main__':
    unittest.main()
