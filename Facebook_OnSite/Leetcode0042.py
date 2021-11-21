class Solution(object):
    def trap(self, height):
        """
        :type height: List[int]
        :rtype: int
        """
        l, r = 0, len(height) - 1

        l_max, r_max = height[0], height[-1]
        rst = 0
        while l <= r:
            lheight = height[l]
            rheight = height[r]

            if l_max <= r_max:
                if l_max >= lheight:
                    rst += l_max - lheight
                else:
                    l_max = lheight
                l += 1
            else:
                if r_max >= rheight:
                    rst += r_max - rheight
                else:
                    r_max = rheight
                r -= 1

        return rst

S = Solution()
height = [4,2,0,3,2,5]
print(S.trap(height))
height = [0,1,0,2,1,0,1,3,2,1,2,1]
print(S.trap(height))