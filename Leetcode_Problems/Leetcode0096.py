class Solution(object):
    def numTrees(self, n):
        """
        :type n: int
        :rtype: int
        """
        
        # factorials = [1] * (n + 1)
        # for i in range(1, len(factorials)):
        #     factorials[i] = i  * factorials[i-1]
        ans = [0] * (n + 1)
        ans[0] = ans[1] = 1

        for i in range(2, n + 1):
            breakdown = [ans[j-1] * ans[i-j] for j in range(1, i + 1)]
            ans[i] = sum(breakdown)

        return ans[-1]