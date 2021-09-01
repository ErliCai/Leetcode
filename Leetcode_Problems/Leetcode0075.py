class Solution(object):
    def sortColors(self, nums):
        """
        :type nums: List[int]
        :rtype: None Do not return anything, modify nums in-place instead.
        """
        
        n_0 = 0
        n_1 = 0
        n_2 = 0

        for n in nums:
            if n == 0:
                n_0 += 1
            elif n == 1:
                n_1 += 1
            else:
                n_2 += 1

        for i in range(len(nums)):
            if i < n_0:
                nums[i] = 0
            elif i < n_0 + n_1:
                nums[i] = 1
            else:
                nums[i] = 2


#solution2
class Solution(object):
    def sortColors(self, nums):
        """
        :type nums: List[int]
        :rtype: None Do not return anything, modify nums in-place instead.
        """

        i, j, k = 0, len(nums) - 1

        while j <= k:
            if nums[j] == 0:
                j += 1
            elif nums[j] == 1:
                nums[j], nums[i] = nums[i], nums[j]
                i += 1
                j += 1
            else:
                nums[j], nums[k] = nums[k], nums[j]
                j += 1
                k -= 1