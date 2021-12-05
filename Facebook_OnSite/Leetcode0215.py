class Solution(object):
    def findKthLargest(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: int
        """
        return self.partition(nums, k)

    def partition(self, nums, k):
        index = len(nums) // 2

        larger = []
        smaller = []
        for i in range(len(nums)):
            if i != index:
                if nums[i] > nums[index]:
                    larger.append(nums[i])
                else:
                    smaller.append(nums[i])

        if len(larger) == k-1:
            return nums[index]
        elif len(larger) > k-1:
            return self.partition(larger, k)
        else:
            return self.partition(smaller, k - 1 - len(larger))



S = Solution()
nums = [3,2,1,5,6,4]
k = 2
print(S.findKthLargest(nums, k))