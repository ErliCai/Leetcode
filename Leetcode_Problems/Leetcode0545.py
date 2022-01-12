# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution(object):
    def boundaryOfBinaryTree(self, root):
        """
        :type root: TreeNode
        :rtype: List[int]
        """
        
        #print(self.leftBoundary(root.left), self.leaves(root), self.rightBoundary(root.right))
        leaves = self.leaves(root)
        if not root.left and not root.right:
            leaves = []

        self.boundaries = [root.val] + self.leftBoundary(root.left) + leaves + self.rightBoundary(root.right)
        return self.boundaries

    def leftBoundary(self, root):

        if not root:
            return []

        if root.left:
            return [root.val] + self.leftBoundary(root.left)
        elif root.right:
            return [root.val] + self.leftBoundary(root.right)
        else:
            return []

    def leaves(self, root):
        
        if not root.left and not root.right:
            return [root.val]
        
        lf = []
        rf = []
        if root.left:
            lf = self.leaves(root.left)
        if root.right:
            rf = self.leaves(root.right)
        return lf + rf
                

    def rightBoundary(self, root):

        if not root:
            return []
         
        if root.right: 
            return self.rightBoundary(root.right) + [root.val]
        elif root.left:
            #print(root.val)
            return self.rightBoundary(root.left) + [root.val]
        else:
            return []