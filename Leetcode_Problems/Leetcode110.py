# Definition for a binary tree node.
class TreeNode(object):
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
class Solution(object):
    def isBalanced(self, root):
        """
        :type root: TreeNode
        :rtype: bool
        """

        def helper(node):
            if not node.left and not node.right:
                return True, 1
            
            if node.left:
                bl, hl = helper(node.left)
            else:
                bl, hl = True, 0

            if node.right:
                br, hr = helper(node.right)
            else:
                br, hr = True,0

            if abs(hl- hr) <= 1 and br and bl:
                return True, hl
            else:
                return False, max(hl,hr) + 1

        return helper(root)[0]
