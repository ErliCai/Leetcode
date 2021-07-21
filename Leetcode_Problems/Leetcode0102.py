# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def levelOrder(self, root):
        """
        :type root: TreeNode
        :rtype: List[List[int]]
        """
        
        if not root:
            return []
        
        level = [root]
        answer = []

        while level:

            temp_level = []
            level_val = []

            for l in level:
                level_val.append(l.val)
                if l.left:
                    temp_level.append(l.left)
                if l.right:
                    temp_level.append(l.right)
            level = temp_level
            answer.append(level_val)

        return answer