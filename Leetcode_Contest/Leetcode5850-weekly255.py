class Solution(object):
    def findGCD(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        
        def Euclid(i, j):
            i, j = max(i, j), min(i, j)
            r = i % j
            if r == 0:
                return j
            else:
                return Euclid(j, r)
        
        i, j = min(nums), max(nums)

        return Euclid(i, j)