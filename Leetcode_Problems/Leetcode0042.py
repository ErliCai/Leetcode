from smtplib import LMTP_PORT


class Solution(object):
    def trap(self, height):
        """
        :type height: List[int]
        :rtype: int
        """

        trapped = 0
        if len(height) <= 2:
            return 0
        

        i, j = 0, len(height) - 1
        l_max, r_max = height[i], height[j] 
        while i < j:
            if l_max <= r_max:
                i += 1
                if height[i] > l_max:
                    l_max = height[i]
                else:
                    trapped += l_max - height[i]
                    
            else:
                j -= 1
                if height[j] > r_max:
                    r_max = height[j]
                else:
                    trapped += r_max - height[j]
            print(i,j,trapped)

        return trapped

S = Solution()
height = [0,1,0,2,1,0,1,3,2,1,2,1]
S.trap(height)
