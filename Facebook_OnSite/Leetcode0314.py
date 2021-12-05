
# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def verticalOrder(self, root):
        """
        :type root: TreeNode
        :rtype: List[List[int]]
        """

        level = [(root, 0)]
        
        postive_pos = []
        negative_pos = []

        while level:
            new_level = []

            for node, pos in level:
                
                if node.left:
                    new_level.append((node.left, pos-1))

                if node.right:
                    new_level.append((node.right, pos+1))

                if pos >= 0:
                    if pos >= len(postive_pos):
                        postive_pos.append([])
                    postive_pos[pos].append(node.val)
                else:
                    if -pos >= len(negative_pos) + 1:
                        negative_pos.append([])
                    negative_pos[-pos-1].append(node.val)
            

            level = new_level

        return negative_pos[::-1] + postive_pos