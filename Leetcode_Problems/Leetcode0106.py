# Definition for a binary tree node.
class TreeNode(object):
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution(object):
    def buildTree(self, inorder, postorder):
        """
        :type inorder: List[int]
        :type postorder: List[int]
        :rtype: TreeNode
        """

        if len(inorder) == 0:
            return None
        if len(inorder) == 1:
            return TreeNode(inorder[0])
        
        i = inorder.index(postorder[-1])
        left_child = self.buildTree(inorder[:i], postorder[:i])
        right_child = self.buildTree(inorder[i+1:], postorder[i:-1])

        return TreeNode(postorder[-1], left_child, right_child)