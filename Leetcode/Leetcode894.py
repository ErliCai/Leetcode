# Definition for a binary tree node.
class TreeNode(object):
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
class Solution(object):
    def allPossibleFBT(self, n):
        """
        :type n: int
        :rtype: List[TreeNode]
        """
        
        if n // 2:
            return []
        if n == 1:
            return [TreeNode()]

        forest = self.allPossibleFBT(n-2)

        for f in forest:
            return



a = [[1]]

b = [[1]]

print(a == b)