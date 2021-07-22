# Definition for a binary tree node.
class TreeNode(object):
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution(object):
    def lowestCommonAncestor(self, root, p, q):
        """
        :type root: TreeNode
        :type p: TreeNode
        :type q: TreeNode
        :rtype: TreeNode
        """
        if not isinstance(p, int):
            p, q = min(p.val, q.val), max(p.val, q.val)

        if p <= root.val <= q:
            return root
        if root.val < p:
            return self.lowestCommonAncestor(root.right, p, q)
        if root.val > q:
            return self.lowestCommonAncestor(root.left, p, q)