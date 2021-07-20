class Solution(object):
    def permute(self, nums):
        """
        :type nums: List[int]
        :rtype: List[List[int]]
        """

        l = []
        self.backtrack(l, nums, [], len(nums))
        return l


    def backtrack(self, l, rnums, temp, n):
        
        if len(temp) == n:

            l.append(temp)
        
        else:
            for i in range(len(rnums)):
                rnums_copy = rnums[::]
                a = rnums_copy.pop(i)
                self.backtrack(l, rnums_copy, temp + [a], n)

S = Solution()
nums = [1,2,3]
print(S.permute(nums))