"""
# Definition for a Node.
class Node(object):
    def __init__(self, val=None, children=None):
        self.val = val
        self.children = children
"""

class Solution(object):
    def postorder(self, root):
        """
        :type root: Node
        :rtype: List[int]
        """
        
        if not root:
            return []

        if root.children:
            l = []
            for i in root.children:
                l += self.postorder(i)
            return l + [root.val]
        else:
            return [root.val]