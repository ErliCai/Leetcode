# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def diameterOfBinaryTree(self, root):
        """
        :type root: TreeNode
        :rtype: int
        """
        self.height(root)
        max_diameter = 0
        queue = [root]
        while queue:
            r = queue.pop()
            left, right = r.left, r.right
            if left:
                queue.append(left)
            if right:
                queue.append(right)
            if left and right:
                v = left.val + right.val
                max_diameter = max(v, max_diameter)
        return max_diameter
        
    def height(self, root):

        left, right = root.left, root.right
        if not left and not right:
            root.val = 1
        
        elif not left:
            self.height(right)
            root.val = right.val + 1
        elif not right:
            self.height(left)
            root.val = left.val + 1
        else:

            self.height(left)
            self.height(right)
            root.val = max(left.val, right.val) + 1


class Solution2(object):
    def diameterOfBinaryTree(self, root):
        """
        :type root: TreeNode
        :rtype: int
        """

        self.ans = 0
        def height(root):
            if not root:
                return 0
            left = height(root.left)
            right = height(root.right)
            self.ans = max(self.ans, left + right)

            return max(left, right) + 1

        height(root)
        return self.ans