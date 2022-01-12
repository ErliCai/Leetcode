class Solution(object):
    def sumZero(self, n):
        """
        :type n: int
        :rtype: List[int]
        """
        
        rst = [i for i in range(1,n)]
        rst += [-sum(rst)]

        return rst


S = Solution()
print(S.sumZero(10))