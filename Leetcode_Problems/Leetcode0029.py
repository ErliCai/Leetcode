class Solution(object):
    def divide(self, dividend, divisor):
        """
        :type dividend: int
        :type divisor: int
        :rtype: int
        """
        
        if dividend == 0:
            return 0
        
        minus_sign = False
        if (dividend < 0 and divisor > 0) or (divisor < 0 and dividend > 0):
            minus_sign = True

        dividend, divisor = abs(dividend), abs(divisor)

        count = 0
        while dividend >= 0 :
            dividend = dividend - divisor
            count += 1
        count -= 1
        if minus_sign:
            count = -count
        return count