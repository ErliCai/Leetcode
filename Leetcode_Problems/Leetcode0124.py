# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def maxPathSum(self, root):
        """
        :type root: TreeNode
        :rtype: int
        """
        
        self.max = None
        return self.helper(root)[0]
        

    def helper(self, root):

        if not root.left and not root.right:
            if self.max == None:
                self.max = root.val
            else:
                self.max = max(root.val, self.max)
            return root.val
        else:
            l_max_to_leaf, r_max_to_leaf = 0, 0
            if root.left:
                l_max_to_leaf = self.helper(root.left)
            if root.right:
                r_max_to_leaf = self.helper(root.right)

            self.max = max(self.max, l_max_to_leaf + r_max_to_leaf + root.val)
            return max(l_max_to_leaf, r_max_to_leaf) + root.val