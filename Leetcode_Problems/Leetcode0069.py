class Solution(object):
    def mySqrt(self, x):
        """
        :type x: int
        :rtype: int
        """
        
        
        
        lower = 0
        higher = 2 ** 30
        
        while lower <= higher:
            mid = lower + higher

            if mid ** 2 < x < (mid + 1) ** 2:
                return mid
            elif mid ** 2 < x:
                lower = mid + 1
            else:
                higher = mid - 1