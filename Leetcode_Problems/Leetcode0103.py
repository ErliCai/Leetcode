# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def zigzagLevelOrder(self, root):
        """
        :type root: TreeNode
        :rtype: List[List[int]]
        """

        if not root:
            return []
        
        level = [root]
        answer = []

        reversed = True
        while level:

            reversed = not reversed
            temp_level = []
            level_val = []

            for l in level:
                if l.left:
                    temp_level.append(l.left)
                if l.right:
                    temp_level.append(l.right)
                level_val.append(l.val)

            if reversed:
                answer.append(level_val[::-1])
            else:
                answer.append(level_val)
            
            level = temp_level

        return answer 
