# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution(object):
    def countNodes(self, root):
        """
        :type root: TreeNode
        :rtype: int
        """
        if self.height(root) == 0:
            return 0
        left_height = self.height(root.left)
        right_height = self.height(root.right)
        #print(left_height, right_height)
        if left_height == right_height:
            return self.num_nodes_fully_complete(left_height) + self.countNodes(root.right) + 1
        else:
            return self.num_nodes_fully_complete(right_height) + self.countNodes(root.left) + 1

    def height(self, root):
        if root:
            return self.height(root.left) + 1
        else:
            return 0

    def num_nodes_fully_complete(self, n):
        ans = 0
        for i in range(n):
            ans *= 2
            ans += 1
        return ans