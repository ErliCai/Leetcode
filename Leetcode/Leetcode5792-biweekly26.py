class Solution(object):
    def countTriples(self, n):
        """
        :type n: int
        :rtype: int
        """

        count = 0
        for i in range(1,n):
            for j in range(i+1, n+1):
                for k in range(j+1,n+1):
                    if i*i + j*j == k*k:
                        count += 1


        return count * 2
    

S = Solution()
n = 10
print(S.countTriples(n))