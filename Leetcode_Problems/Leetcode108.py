# Definition for a binary tree node.
class TreeNode(object):
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution(object):
    def sortedArrayToBST(self, nums):
        """
        :type nums: List[int]
        :rtype: TreeNode
        """
        
        i = len(nums) // 2
        root = TreeNode(val = nums[i])
        if i != 0:
            print(nums[:i])
            root.left = self.sortedArrayToBST(nums[:i])
        if i != len(nums)-1:
            root.right = self.sortedArrayToBST(nums[i+1:])

        return root

