# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def maxDepth(self, root):
        """
        :type root: TreeNode
        :rtype: int
        """
        
        round = 0
        queue = [root]
        while queue:
            temp_q = []
            for q in queue:
                if q.left:
                    temp_q.append(q.left)
                if q.right:
                    temp_q.append(q.right)

            queue = temp_q
            round += 1
        
        return round