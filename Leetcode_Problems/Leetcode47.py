class Solution(object):
    def permuteUnique(self, nums):
        """
        :type nums: List[int]
        :rtype: List[List[int]]
        """

        nums.sort()
        l = []
        self.backtrack(l, nums, [])
        return l

    def backtrack(self, accumulator, nums, temp):

        if not nums:
            accumulator.append(temp)

        for i in range(len(nums)):
            if i != 0  and nums[i] == nums[i-1]:
                continue
            else:
                nums_copy = nums[::]
                nums_copy.pop(i)
                self.backtrack(accumulator, nums_copy, temp + [nums[i]])

S = Solution()
nums = [1,1,2]
a = S.permuteUnique(nums)
print(a)