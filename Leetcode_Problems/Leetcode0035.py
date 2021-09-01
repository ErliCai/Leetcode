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


# second time
class Solution(object):
    def searchInsert(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: int
        """

        low, high = 0, len(nums) - 1

        while low <= high:
            mid = (low+ high) / 2

            if nums[mid] == target:
                return mid
            elif nums[mid] < target:
                low = mid + 1
            else:
                high = mid - 1

            
        return low

# third time
class Solution(object):

    def searchInsert(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: int
        """

        low, high = 0, len(nums) - 1

        while low <= high:
            mid = (low + high) // 2

            if nums[mid] > target and mid == 0:
                return 0
            elif nums[mid] < target and mid == len(nums) - 1:
                return len(nums)
            elif nums[mid] < target and nums[mid + 1] >= target:
                return mid + 1
            elif nums[mid] > target:
                high = mid - 1
            else:
                low = mid + 1
