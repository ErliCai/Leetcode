class Solution(object):
    def search(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: int
        """
        pivot = 0
        for i in range(1, len(nums)):
            if nums[i] < nums[i-1]:
                pivot = i
                break
        n = len(nums) - pivot
        nums_sorted = nums[pivot:] + nums[:pivot]
        index = self.binarySearch(nums_sorted, target)
        if index == -1:
            return -1
        else:
            if index >= n:
                return index - n
            else:
                return pivot + index
        
        
    def binarySearch(self, nums, target):
        
        #print(nums)

        lower = 0
        upper = len(nums) - 1

        while lower <= upper:
            mid = (lower + upper) // 2
            if nums[mid] == target:
                return mid
            elif nums[mid] < target:
                lower = mid + 1
            else:
                upper = mid - 1

        return -1

S = Solution()
print(S.binarySearch([3,1], 3))