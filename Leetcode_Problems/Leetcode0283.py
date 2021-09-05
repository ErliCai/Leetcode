class Solution(object):
    def moveZeroes(self, nums):
        """
        :type nums: List[int]
        :rtype: None Do not return anything, modify nums in-place instead.
        """
        i, j = 0, 0
        while i < len(nums):
            if nums[i] == 0:
                i += 1
            else:
                nums[j] = nums[i]
                j += 1
                i += 1

        while j < len(nums):
            nums[j] = 0
            j += 1
