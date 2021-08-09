class Solution(object):
    def maximumGap(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        
        l = [[] for i in range(len(nums))]
        max_num = max(nums)
        gap = (max_num // len(nums)) + 1

        for i in nums:
            l[i // gap].append(i)

        l = [sorted(i) for i in l if i != []]
        if len(l) == 1:
            return 1

        max_gap = 0
        for i in range(1,len(l)):
            candidate = l[i][0] - l[i-1][-1]
            max_gap = max(max_gap, candidate)

        return max_gap


S = Solution()
nums = [3,6,9,1,2]
print(S.maximumGap(nums))
