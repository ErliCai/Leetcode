class Solution(object):
    def search(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: int
        """
        
        low = 0
        high = len(nums) - 1

        while low <= high:

            mid = (low + high) // 2
            print(mid, nums[mid])
            if nums[mid] < target:
                low = mid + 1
            elif nums[mid] > target:
                high = mid -1
            else:
                return mid
        return -1

S = Solution()
nums = [5]
target = 5
result = S.search(nums, target)          
print(result)


# second time
class Solution(object):
    def search(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: int
        """

        low, high = 0, len(nums) - 1

        while low <= high:
            mid = (low + high) / 2
            if nums[mid] == target:
                return mid
            elif nums[mid] > target:
                high = mid - 1
            else:
                low =  mid + 1
        
        return -1