# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def buildTree(self, preorder, inorder):
        """
        :type preorder: List[int]
        :type inorder: List[int]
        :rtype: TreeNode
        """

        if not preorder:
            return None
        
        i = inorder.index(preorder[0])
        left = self.buildTree(preorder[1:i+1], inorder[:i])
        right = self.buildTree(preorder[i+1:], inorder[i+1:])

        return TreeNode(preorder[0], left, right)
