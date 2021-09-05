class Solution(object):
    def rotate(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: None Do not return anything, modify nums in-place instead.
        """
        
        k = k % len(nums)
        n1 = nums[-k:]
        n2 = nums[:-k]
        if n2:
            for i in range(len(nums) - k):
                nums[k + i] = n2[i]
        if n1:
            for i in range(k):
                nums[i] = n1[i]
