class Solution(object):
    def maxUniqueSplit(self, s):
        """
        :type s: str
        :rtype: int
        """

        self.cnt = 0
        self.backtracking(set(), s, 0)
        
        return self.cnt

    def backtracking(self, s, r, c):

        if not r:
            self.cnt = max(self.cnt, c)

        else:
            for i in range(len(r)):
                if r[:i+1] not in s:
                    s.add(r[:i+1])
                    self.backtracking(s, r[i+1:] , c+1)
                    s.remove(r[:i+1])

S = Solution()
s = "ababccc"
print(S.maxUniqueSplit(s))
