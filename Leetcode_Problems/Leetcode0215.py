class Solution(object):

    def __init__(self):
        self.k_largest = []

    def findKthLargest(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: int
        """
        
        self.k_largest = nums[:k]
        self.k_largest.sort()

        for i in range(k, len(nums)):
            if nums[i] > self.k_largest[-1]:
                self.insert_k(nums[i])

        return self.k_largest[-1]

    def binary_search(self, n):
        if self.k_largest[0] < n:
            return 0

        low, high = 0, len(self.k_largest)

        while low <= high:
            mid = (low + high) / 2

            if self.k_largest[mid] < n:
                low = mid + 1

            elif self.k_largest[mid] > n:
                high = mid - 1

        if self.k_largest[low] > n:
            return low - 1
        else:
            return low

    def insert_k(self, n):
        i = self.binary_search(n)
        self.k_largest.insert(i, n)
        self.k_largest.pop(0)

            


