import random

class Solution(object):

    def __init__(self, w):
        """
        :type w: List[int]
        """
        
        self.range = []
        sum = 0
        for i in w:
            self.range.append(sum)
            sum += i
        self.range.append(sum)
        

    def pickIndex(self):
        """
        :rtype: int
        """
        target = random.random() * self.range[-1]
        return self.binarySearch(self,range, target)
    
    def binarySearch(self, nums, target):

        low, high = 0, len(nums) - 1
        while low < high:
            mid = (low + high + 1) // 2
            if mid == low:
                break
            if nums[mid] == target:
                low = mid
                return nums[low]
            elif nums[mid] < target:
                low = mid
            else:
                high = mid - 1

        return nums[low]
        
# Your Solution object will be instantiated and called as such:
# obj = Solution(w)
# param_1 = obj.pickIndex()

S = Solution([1])
nums = [1,2,3,4,5,6,7,89]

S.binarySearch(nums, 3.5)