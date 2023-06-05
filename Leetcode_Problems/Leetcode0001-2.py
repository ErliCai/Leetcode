class Solution(object):
    def twoSum(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[int]
        """
        
        s = set(nums)

        for i in range(len(nums)):
            if target - nums[-1-i] in nums:

                if nums.index(target - nums[-1-i]) != len(nums)-1-i:
                    return [nums.index(target - nums[-1-i]), len(nums)-1-i]