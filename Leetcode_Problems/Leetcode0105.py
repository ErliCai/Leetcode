# Definition for a binary tree node.
class TreeNode(object):
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution(object):
    def buildTree(self, preorder, inorder):
        """
        :type preorder: List[int]
        :type inorder: List[int]
        :rtype: TreeNode
        """
        
        def buildTree(preorder, inorder):
            if len(preorder) == 1:
                return TreeNode(preorder[0])
            if len(preorder) == 0:
                return None

            in_index = inorder.index(preorder[0])

            left_child = buildTree(preorder[1:in_index+1], inorder[:in_index])
            right_child = buildTree(preorder[in_index+1:], inorder[in_index+1:])
            return TreeNode(preorder[0], left_child, right_child)

        return buildTree(preorder, inorder)
            