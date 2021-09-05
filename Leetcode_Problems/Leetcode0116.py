"""
# Definition for a Node.
class Node(object):
    def __init__(self, val=0, left=None, right=None, next=None):
        self.val = val
        self.left = left
        self.right = right
        self.next = next
"""

class Solution(object):
    def connect(self, root):
        """
        :type root: Node
        :rtype: Node
        """
        r = root
        h = 0
        while r:
            r = r.left
            h += 1

        level = [root]
        for n in range(h - 1):
            next_level = []
            for node in level:
                next_level.append(node.left)
                next_level.append(node.right)
                if node.next:
                    node.left.next, node.right.next = node.right, node.next.left
                else:
                    node.left.next = node.right
            level = next_level

        return root


class Solution(object):
    def connect(self, root):
        """
        :type root: Node
        :rtype: Node
        """

        level = [root,None]
        while len(level) > 1:
            next_level = []
            for i in range(len(level) - 1):
                level[i].next = level[i+1]
                if level[i].left:
                    next_level.append(level[i].left)
                if level[i].right:
                    next_level.append(level[i].right)

            level = next_level + [None]