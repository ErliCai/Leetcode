# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def diameterOfBinaryTree(self, root):
        """
        :type root: TreeNode
        :rtype: int
        """
        self.diameter = 0
        self.postorder(root)
        return self.diameter
        
    def postorder(self, root):
        
        left_depth = right_depth = 0

        if root.left:
            left_depth = self.postorder(root.left) + 1
        if root.right:
            right_depth = self.postorder(root.right) + 1

        print(root.val, left_depth, right_depth)
        
        self.diameter = max(self.diameter, (left_depth + right_depth))

        return max(left_depth, right_depth) + 1