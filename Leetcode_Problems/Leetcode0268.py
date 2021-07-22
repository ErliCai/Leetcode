class Solution(object):
    def missingNumber(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """

        s = sum(nums)
        n = len(nums)
        return n * (n + 1) - s