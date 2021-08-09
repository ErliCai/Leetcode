# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def widthOfBinaryTree(self, root):
        """
        :type root: TreeNode
        :rtype: int
        """
        level = [[root, 1]]
        max_width = 1
        while level:
            next_level = []
            for node, pos in level:
                if node.left:
                    next_level.append([node.left, pos * 2 - 1])
                if node.right:
                    next_level.append([node.right, pos * 2])
            if next_level:
                left_most = next_level[0]
                right_most = next_level[-1]
                width_current_level = right_most[1] - left_most[1] + 1
                max_width = max(width_current_level, max_width)

                left_most_v = left_most[1] + 1
                for node in next_level:
                    node[1] -= (left_most_v - 1)
            
            level = next_level

        return max_width