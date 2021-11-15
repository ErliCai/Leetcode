class Solution(object):

    def findPeakElement(self, nums):
        if self.peak_check(nums, 0):
            return 0
        if self.peak_check(nums, len(nums) - 1):
            return len(nums) - 1

        return self.findPeakElement_recursion(nums) 



    def findPeakElement_recursion(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        
        low, high = 0, len(nums) - 1
        if high - low <= 3:
            return nums.index(max(nums))

        l, r = (low+high) / 3, 2 * (low+high) / 3

        if nums[low] > nums[l]:
            if self.peak_check(nums,l):
                return l
            else:
                return self.findPeakElement_recursion(nums[:l+1])

        elif nums[low] > nums[r]:
            if self.peak_check(nums,r):
                return r
            else:
                return self.findPeakElement_recursion(nums[:r+1])

        elif nums[high] > nums[r]:
            if self.peak_check(nums,r):
                return r
            else:
                return r + self.findPeakElement_recursion(nums[r:])

        elif nums[high] > nums[l]:
            if self.peak_check(nums,l):
                return l
            else:
                return l + self.findPeakElement_recursion(nums[l:])

        elif nums[l] >= nums[r]:
            if self.peak_check(nums,r):
                return r
            else:
                return self.findPeakElement_recursion(nums[:r+1])

        elif nums[l] <= nums[r]:
            if self.peak_check(nums,r):
                return r
            else:
                return l + self.findPeakElement_recursion(nums[l:])


    def peak_check(self, nums, i):

        """
        O(1) time
        """

        if len(nums) == 1:
            return 0
        
        if i == 0:
            return nums[i] > nums[i+1]

        elif i == len(nums) - 1:
            return nums[i] > nums[i-1]

        else:
            return nums[i] > nums[i-1] and nums[i] > nums[i+1]
            
      