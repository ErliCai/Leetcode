# Definition for a binary tree node.
class TreeNode(object):
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
class Solution(object):
    def mergeTrees(self, root1, root2):
        """
        :type root1: TreeNode
        :type root2: TreeNode
        :rtype: TreeNode
        """
        if not root1 and not root2:
            return
        root = TreeNode()
        q = [(root, root1, root2)]
        while q:
            r, r1, r2 = q.pop()

            v1, v2 = 0, 0
            r1left = r1right = r2left = r2right = None
            if r1:
                v1 = r1.val
                r1left = r1.left
                r1right = r1.right
            if r2:
                v2 = r2.val
                r2left = r2.left
                r2right = r2.right
            r.val = v1 + v2
            if r1left or r2left:
                r.left = TreeNode()
                q.append((r.left, r1left, r2left))
            if r1right or r2right:
                r.right = TreeNode()
                q.append((r.right, r1right, r2right))


        return root


class Solution2(object):
    def mergeTrees(self, root1, root2):
        """
        :type root1: TreeNode
        :type root2: TreeNode
        :rtype: TreeNode
        """

        if root1 and root2:
            r = TreeNode(root1.val + root2.val)
            r.left = self.mergeTrees(root1.left, root2.left)
            r.right = self.mergeTrees(root1.right, root2.right)
            return r
        else:
            return root1 or root2


class Solution3(object):
    def mergeTrees(self, root1, root2):
        """
        :type root1: TreeNode
        :type root2: TreeNode
        :rtype: TreeNode
        """

        if not root1 and not root2:
            return None
        elif root1 and not root2:
            return TreeNode(root1.val, self.mergeTrees(root1.left, None), self.mergeTrees(root1.right, None))
        elif root2 and not root1:
            return TreeNode(root2.val,self.mergeTrees(root2.left, None), self.mergeTrees(root2.right, None))
        else:
            return TreeNode(root1.val+root2.val, self.mergeTrees(root1.left, root2.left), self.mergeTrees(root1.right, root2.right))