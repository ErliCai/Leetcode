# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def distributeCoins(self, root):
        """
        :type root: TreeNode
        :rtype: int
        """

        self.rst = 0
        self.count(root)

        return self.rst

    def count(self, root):

        if not root.left and not root.right:
            return root.val, 1

        else:
            lc = ln = rc = rn = 0
            if root.left:
                lc, ln = self.count(root.left)
            if root.right:
                rc, rn = self.count(root.right)
                
            #print(root.val, self.rst, rn,rc,ln,lc)
            self.rst += abs(rc - rn) + abs(lc- ln)

            return lc + rc + root.val, ln + rn + 1