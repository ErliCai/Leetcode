# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def rightSideView(self, root):
        """
        :type root: TreeNode
        :rtype: List[int]
        """
        
        q = [root]
        a = []
        while q:
            temp_q = []
            v = []
            for i in range(len(q)):
                node = q.pop()
                if node.left:
                    temp_q.append(node.left)
                    v.append(node.left.val)
                if node.right:
                    temp_q.append(node.right)
                    v.append(node.right.val)

            a.append(v[-1])
            
        return a