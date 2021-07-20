class Solution(object):
    def repeatedSubstringPattern(self, s):
        """
        :type s: str
        :rtype: bool
        """
        
        l = 0
        for i in range(len(s)-1):
            print(s[:i+1], s[-i-1:])
            if s[:i+1] == s[-i-1:]:
                l = i + 1

        return True if l != 0 and (len(s) % (len(s) - l) == 0) else False


S = Solution()
s = "abab"
answer = S.repeatedSubstringPattern(s)
print(answer)