# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def verticalTraversal(self, root):
        """
        :type root: TreeNode
        :rtype: List[List[int]]
        """
        self.rst = {}
        level = [(root,0)]
        while level:
            pos_occupied = {}
            next_leval = []
            for node, pos in level:
                if pos not in pos_occupied:
                    pos_occupied[pos_occupied] = []
                pos_occupied[pos_occupied].append(node.val)
            if node.left:
                next_leval.append[root.left, pos-1]
            if node.right:
                next_leval.append[root.right, pos+1]
            for i in pos_occupied:
                if i not in self.rst:
                    self.rst[i] = []
                self.rst[i] += sorted(pos_occupied[i])
            level = next_leval

        
        return [self.rst[k] for k in sorted(self.rst.keys())]
