class Solution(object):
    def nextPermutation(self, nums):
        """
        :type nums: List[int]
        :rtype: None Do not return anything, modify nums in-place instead.
        """

        # [1,2,3,4] -> [1,2,4,3] -> [1,3,2,4] -> [1,3,4,2] -> [1,4,2,3]

        n = len(nums)
        indedx = 0
        for i in range(n-1):
            if nums[-1-i] > nums[-2-i]:
                index = -i-1
                break

S = Solution()
nums = [1,2,3,4]
print(S.nextPermutation(nums))