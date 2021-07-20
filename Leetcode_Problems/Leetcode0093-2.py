class Solution(object):
    def restoreIpAddresses(self, s):
        """
        :type s: str
        :rtype: List[str]
        """
        l = []
        self.backtrack(l, "", s, 1)

        return l

    def backtrack(self, accumulator, a, s, n):
        if n == 4 and self.valid(s):
            accumulator.append(a[1:]+"."+s)
        
        elif n < 4:
            for i in range(3):
                if i <= len(s) and self.valid(s[:i+1]):
                    self.backtrack(accumulator, a+"."+s[:i+1], s[i+1:], n+1)

        
    def valid(self, s):
        if not s:
            return False
        if s == "0":
            return True
        elif s[0] == "0":
            return False
        elif int(s) <= 255:
            return True
        else:
            return False

S = Solution()
s = "1111"
print(S.restoreIpAddresses(s))