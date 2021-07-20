class Solution(object):
    def subsets(self, nums):
        """
        :type nums: List[int]
        :rtype: List[List[int]]
        """

        if len(nums) == 1:
            return [[], nums]

        n = nums.pop()
        subsets_one_less_element = self.subsets(nums)
        print(subsets_one_less_element)

        a = []
        for i in subsets_one_less_element:
            j = i[::]
            j.append(n)
            a.append(j)

        return a + subsets_one_less_element

class Solution2(object):
    def subsets(self, nums):
        """
        :type nums: List[int]
        :rtype: List[List[int]]
        """

        n = len(nums)
        a = []
        for i in range(2 ** n):
            b = bin(i)[2:]
            c = []
            for j in range(len(b)):
                if b[j] == "1":
                    c.append(nums[len(b)-j-1])

            a.append(c)
        return a



S = Solution2()
nums = [1,2,3,4]
print(S.subsets(nums))
