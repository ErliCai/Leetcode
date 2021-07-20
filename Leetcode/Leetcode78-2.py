class Solution(object):
    def subsets(self, nums):
        """
        :type nums: List[int]
        :rtype: List[List[int]]
        """
        l = []
        self.backtrack(nums, l, [], 0)
        return l

    def backtrack(self, num, l, templ, i):
        print(i, templ)
        l.append(templ[::])
        j = i
        while j < len(num):
            templ.append(num[j])
            self.backtrack(num, l, templ, j+1)
            templ.pop()
            j += 1


S = Solution()
nums = [1, 2]
print(S.subsets(nums))
