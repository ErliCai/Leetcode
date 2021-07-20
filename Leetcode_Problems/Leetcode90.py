class Solution(object):
    def subsetsWithDup(self, nums):
        """
        :type nums: List[int]
        :rtype: List[List[int]]
        """
        l = []
        sorted(nums)
        self.backtracking(nums, l, [], 0)
        return l

    def backtracking(self, nums, l, templ, i):

        l.append(templ[::])
        j = i

        while j < len(nums):
            if j != i and nums[j] == nums[j-1]:
                j += 1
                continue
            templ.append(nums[j])
            self.backtracking(nums, l, templ, j+1)
            templ.pop()
            j += 1


S = Solution()
nums = [1, 2, 2]
print(S.subsetsWithDup(nums))
