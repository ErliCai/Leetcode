# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def binaryTreePaths(self, root):
        """
        :type root: TreeNode
        :rtype: List[str]
        """

        l = []
        self.backtracking(l, "", root)
        return l

    def backtracking(self, accumulator, temp, root):
        arrow = "->"
        new_string = temp + arrow + int(root.val)
        if not root.left and not root.right:
            accumulator.append(new_string)

        if root.left:
            self.backtracking(accumulator, new_string, root.left)

        if root.right:
            self.backtracking(accumulator, new_string, root.right)
