class Solution(object):

    def isSubsequence(self, s, t):

        if not s:
            return True
        if not t:
            return False 

        if s[0] == t[0]:
            return self.isSubsequence(s[1:], t[1:])
        else:
            return self.isSubsequence(s, t[1:])
            