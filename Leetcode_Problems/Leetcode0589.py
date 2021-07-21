"""
# Definition for a Node.
class Node(object):
    def __init__(self, val=None, children=None):
        self.val = val
        self.children = children
"""

class Solution(object):
    def preorder(self, root):
        """
        :type root: Node
        :rtype: List[int]
        """
        
        if not root:
            return []
        
        if root.children:
            l = []
            for c in root.children:
                l += self.preorder(c)
            return [root.val] + l
        else:
            return [root.val]

class Solution2(object):
    def preorder(self, root):
        """
        :type root: Node
        :rtype: List[int]
        """
        
        queue = [root]
        r = []
        while queue:
            q = queue.pop()
            if q.children:
                queue += q.children[::-1]

            r.append(q.val)

        return r