class Solution(object):
    def numIdenticalPairs(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        
        num_set = set(nums)

        total = 0
        for n in num_set:
            repeats = nums.count(n)
            if repeats > 1:
                total += repeats * (repeats - 1) / 2

        return total