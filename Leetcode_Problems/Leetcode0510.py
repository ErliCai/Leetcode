"""
# Definition for a Node.
class Node:
    def __init__(self, val):
        self.val = val
        self.left = None
        self.right = None
        self.parent = None
"""

class Solution(object):
    def inorderSuccessor(self, node):
        """
        :type node: Node
        :rtype: Node
        """
        
        if node.right:
            n = node.right
            while n.left:
                n = n.left
                return n

        elif node.parent:
            n = node.parent
            if n.right == node:
                return
            else:
                return n
