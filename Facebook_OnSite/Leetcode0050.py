class Solution(object):
    def myPow(self, x, n):
        """
        :type x: float
        :type n: int
        :rtype: float
        """

        if n < 0 :
            return 1 / self.myPow(x, -n) 
        elif n == 0:
            return 1
        elif n == 1:
            return x
        else:
            r, q = n % 2, n // 2
            a = self.myPow(x, r)
            b = self.myPow(x, q) 
            return a * b * b




        
S = Solution()
print(S.myPow(2, -5))