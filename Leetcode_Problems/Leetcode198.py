class Solution(object):
    def rob(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        l = [0] * len(nums)
        l[0] = nums[0]
        l[1] = max(nums[0], nums[1])

        for i in range(2, len(nums) + 1):
            l[i] = max(l[i-1], nums[i]+l[i-2])


        return l[-1]