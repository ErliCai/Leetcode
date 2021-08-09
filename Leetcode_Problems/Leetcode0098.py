# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def isValidBST(self, root):
        """
        :type root: TreeNode
        :rtype: bool
        """

        l = self.inorderTraversal(root)
        for i in range(len(l) - 1):
            if l[i] > l[i+1]:
                return False
        return True
        


    def inorderTraversal(self, root):

        l = []
        r = []
        if root.left:
            l = self.inorderTraversal(root.left)
        if root.right:
            r = self.inorderTraversal(root.right)

        return l + [root.val] + r




class Solution(object):
    def isValidBST(self, root):
        """
        :type root: TreeNode
        :rtype: bool
        """
        low = - 2 ** 31 -1
        high = 2 ** 31
        
        return self.helper(root, low, high)
    
    def helper(self, root, low, high):
        
        
        if not root:
            return True
        elif root.val >= high or root.val <= low:
            return False
        else:
            return self.helper(root.left, low, root.val) and self.helper(root.right, root.val, high)

