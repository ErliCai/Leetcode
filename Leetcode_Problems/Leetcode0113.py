# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def pathSum(self, root, targetSum):
        """
        :type root: TreeNode
        :type targetSum: int
        :rtype: List[List[int]]
        """
        L = []
        self.backtrack(L, root, [], targetSum)
        return L

    def backtrack(self, accumulator, root, temp, target):

        if root:
            # print(root.val, target)

            if root.val == target and not root.left and not root.right:
                accumulator.append(temp + [root.val])
            else:
                self.backtrack(accumulator, root.left, temp + [root.val], target - root.val)
                self.backtrack(accumulator, root.right, temp + [root.val], target - root.val)