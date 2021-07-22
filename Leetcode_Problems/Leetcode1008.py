# Definition for a binary tree node.
class TreeNode(object):
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
class Solution(object):
    def bstFromPreorder(self, preorder):
        """
        :type preorder: List[int]
        :rtype: TreeNode
        """
        
        if len(preorder) == 0:
            return None
        if len(preorder) == 1:
            return TreeNode(preorder[0])

        
        count = 0
        for i in preorder:
            if i < preorder[0]:
                count += 1
            if i > preorder[0]:
                break
        left = self.bstFromPreorder(preorder[1:count+1])
        right = self.bstFromPreorder(preorder[count+1:])
        return TreeNode(preorder[0], left, right)