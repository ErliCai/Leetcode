class Solution(object):
    def minMoves2(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        
        nums.sort()
        n = nums[(len(nums) + 1)// 2]
        rst = 0
        for i in nums:
            rst += abs(i - n)

        return rst

S = Solution()
nums = [1,2,3,1]
print(S.minMoves2(nums))