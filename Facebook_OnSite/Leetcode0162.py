class Solution(object):
    def findPeakElement(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        if nums[0] > nums[1]:
            return nums[0]
        if nums[-1] > nums[-2]:
            return nums[-1]

        return self.recursion(nums)
    
    def recursion(self, nums):

        mid = (len(nums)-1) // 2
        if  nums[mid-1] < nums[mid] and nums[mid] > nums[mid+1]:
            return mid
        elif nums[mid-1] > nums[mid]:
            return self.recursion(nums[:mid+1])
        else:
            return mid + self.recursion(nums[mid:])

