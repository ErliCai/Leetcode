# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def goodNodes(self, root):
        """
        :type root: TreeNode
        :rtype: int
        """

        return self.helper(root, 0)
        
    def helper(self, root, v):

        g_number = 0
        if root.val >= v:
            g_number += 1
        v = max(root.val, v)
        ln = rn = 0
        if root.left:
            ln = self.helper(root.left, v)
        if root.right:
            rn = self.helper(root.right, v)

        return ln + rn + g_number