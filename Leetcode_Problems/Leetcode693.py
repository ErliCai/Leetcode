class Solution(object):
    def hasAlternatingBits(self, n):
        """
        :type n: int
        :rtype: bool
        """
        last_r = None
        q = n
        while q:
            q, r = q // 2, q % 2
            if r == last_r:
                return False
            last_r = r
            
        return True