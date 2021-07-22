# Definition for a binary tree node.
class TreeNode(object):
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution(object):
    def flatten(self, root):
        """
        :type root: TreeNode
        :rtype: None Do not return anything, modify root in-place instead.
        """
        self.flatten_helper(root)
        
    def flatten_helper(self, root):

        if (not root.left) and (not root.right):
            return root
        elif (not root.left) and root.right:
            return self.flatten(root.right)
        elif root.left and (not root.right):
            root.left, root.right = None, root.left
            return self.flatten(root.right)
        else:
            node1 = self.flatten_helper(root.left)
            node2 = self.flatten_helper(root.right)
            root.left, root.right, node1.left, node1.right = None, root.left, None, root.right
            return node2

        