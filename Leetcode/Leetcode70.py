class Solution(object):
    def climbStairs(self, n):
        """
        :type n: int
        :rtype: int
        """

        return self.dp(n)[0]
        
    def dp(self, n):

        if n == 0:
            return 1, 0

        i =  self.dp(n-1)
        return i[0] + i[1], i[0]