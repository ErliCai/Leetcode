# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def rightSideView(self, root):
        """
        :type root: TreeNode
        :rtype: List[int]
        """
        if not root:
            return []
        self.side_view = []
        self.inorder(root, 0)
        return self.side_view
        
    def inorder(self, root, depth):
        
        if depth == len(self.side_view):
            self.side_view.append(0)

        if root.left:
            self.inorder(root.left, depth + 1)
        self.side_view[depth] = root.val
        if root.right:
            self.inorder(root.right, depth + 1)