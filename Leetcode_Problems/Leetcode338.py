class Solution(object):
    def countBits(self, n):
        """
        :type n: int
        :rtype: List[int]
        """
        
        m = 1
        while 2 ** m <= n + 1:
            m += 1

        s = [0]
        for i in range(1, m):
            s = s + [e + 1 for e in s]

        n = n + 1 - 2 ** m
        s =  s + [e+1 for e in s[:n]]
        
        return s

S = Solution()
print(len(S.countBits(127)))
