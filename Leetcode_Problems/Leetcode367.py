class Solution(object):
    def isPerfectSquare(self, num):
        """
        :type num: int
        :rtype: bool
        """      
        
        low = 0
        high = 2**16 - 1

        while low <= high:
            mid = (low + high) // 2
            #print(low, mid, high)
            square = mid * mid
            if square < num: 
                low = mid+1
            elif square > num:
                high = mid-1
            else:
                return True

        return False



S = Solution()
num = 808201
#print(2**16 - 1)
print(S.isPerfectSquare(num)) 