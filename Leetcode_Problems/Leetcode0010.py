class Solution(object):
    def isMatch(self, s, p):
        """
        :type s: str
        :type p: str
        :rtype: bool
        """
        #print(s, p)
        
        if not s and not p:
            return True
        elif not p:
            return False
        elif not s:
            if len(p) > 1 and p[1] == "*":
                return self.isMatch(s, p[2:])
            else:
                return False
        
        else:
            if len(p) > 1 and p[1] == "*":
                if s[0] == p[0] or p[0] == ".":
                    return self.isMatch(s[1:], p) or self.isMatch(s, p[2:])
                else:
                    return self.isMatch(s, p[2:])
            else:
                if s[0] == p[0] or p[0] == ".":
                    return self.isMatch(s[1:], p[1:]) 
                else:
                    return False



S = Solution()

s = "aa" 
p = "a"
print(S.isMatch(s, p))
s = "aa"
p = "a*"
print(S.isMatch(s, p))
s = "ab"
p = ".*"
print(S.isMatch(s, p))
s = "aab"
p = "c*a*b"
print(S.isMatch(s, p))
s = "mississippi"
p = "mis*is*p*."
print(S.isMatch(s, p))