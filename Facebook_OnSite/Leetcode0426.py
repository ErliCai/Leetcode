
# Definition for a Node.
class Node(object):
    def __init__(self, val, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution(object):
    def treeToDoublyList(self, root):
        """
        :type root: Node
        :rtype: Node
        """

        self.last = None
        l = r = root
        while l.left:
            l = l.left
        while r.right:
            r = r.right
        self.inordersort(root)
        l.left, r.right= r, l 
        

    def inordersort(self, root):
        
        if root.left:
            self.inordersort(root.left)

        if self.last is not None:
            self.last.right = root
            root.left = self.last
            self.last = root
        
        if root.rihgt:
            self.inordersort()