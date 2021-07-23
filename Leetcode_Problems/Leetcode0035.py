class Solution(object):
    def searchInsert(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: int
        """

        lower = 0
        upper = len(nums) - 1

        if target < nums[0]:
            return 0
        if target > nums[-1]:
            return len(nums)

        while lower < upper:
            mid = (lower + upper) / 2

            if nums[mid] == target:
                return mid
            elif nums[mid] < target:
                lower = mid + 1
            else:
                upper = mid - 1

            return lower