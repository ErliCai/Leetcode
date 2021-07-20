class Solution(object):
    def reverseStr(self, s, k):
        """
        :type s: str
        :type k: int
        :rtype: str
        """
        
        if len(s) <= k:
            return s[::-1]
        if len(s) <= 2 * k:
            return s[k-1::-1]

        else:
            return s[k-1::-1] + s[k:2*k] + self.reverseStr(s[2*k:], k)

a = "123456"
S = Solution()
print(S.reverseStr(a, 2))