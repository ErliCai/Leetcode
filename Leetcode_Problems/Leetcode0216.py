class Solution(object):
    def combinationSum3(self, k, n):
        """
        :type k: int
        :type n: int
        :rtype: List[List[int]]
        """
        l = []
        self.backtrack(l, [], k, n, 1)
        return l

    def backtrack(self, accumulator, temp, k, n, start):
        #print(k,n,list(temp))

        if k == 0 and n == 0:
            accumulator.append(temp)

        if n > 0:
            for i in range(start, 10):
                if i not in temp and i <= n:
                    self.backtrack(accumulator, temp + [i], k-1, n-i, i+1)

S = Solution()
k, n = 3, 7
print(S.combinationSum3(k, n))