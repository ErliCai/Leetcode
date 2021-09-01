class Solution(object):
    def myPow(self, x, n):
        """
        :type x: float
        :type n: int
        :rtype: float
        """
        
        return x ** n
class Solution(object):
    def myPow(self, x, n):
        """
        :type x: float
        :type n: int
        :rtype: float
        """
        
        return x ** n
    
class Solution(object):
    def myPow(self, x, n):
        """
        :type x: float
        :type n: int
        :rtype: float
        """
        sign = x / abs(x)
        x = abs(x)

        if n == 0:
            return 1
        else:
            r, q = n % 2, n // 2
            if r:
                return sign * x * self.myPow(x, q) ** 2
            else:
                return sign * self.myPow(x, q) ** 2