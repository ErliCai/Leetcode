import random

class Solution(object):

    def findKthLargest(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: int
        """

        rst =self.partition(nums, k)
        return rst
        

    def partition(self, nums, k):

        index = random.randrange(len(nums))
        left = []
        right = []

        n = nums[index]
        for i in range(len(nums)):
            if i != index:
                if nums[i] < n:
                    left.append(nums[i])
                else:
                    right.append(nums[i])

        pos = len(right) + 1
        print(pos, left, right)
        if pos < k:
            return self.partition(left, k - pos) + [n] + right
        elif pos == k:
            return [n] + right
        else:
            return self.partition(right, k)


S = Solution()
nums = [1,3,2,6,4,5]
k = 3
print(S.findKthLargest(nums, k))

