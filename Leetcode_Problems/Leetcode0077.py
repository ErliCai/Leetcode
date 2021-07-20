class Solution(object):
    def combine(self, n, k):
        """
        :type n: int
        :type k: int
        :rtype: List[List[int]]
        """
        l = []
        self.backtrack(l, [], n, k)
        return l
    
    def backtrack(self, accumulator, temp, n, k):
        
        if temp:
            start = temp[-1]
        else:
            start = 0
        for i in range(start+1, n+1):
            print(i, k)
            if k == 1:
                accumulator.append(temp + [i])
            elif k <= n:
                self.backtrack(accumulator, temp+[i], n, k-1)

S = Solution()
n = 3
k = 3
print(S.combine(n,k))