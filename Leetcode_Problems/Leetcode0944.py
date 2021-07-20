class Solution(object):
    def backspaceCompare(self, s, t):
        """
        :type s: str
        :type t: str
        :rtype: bool
        """
        s1 = []
        for i in s:
            if i == "#":
                if s1:
                    s1.pop()
            else:
                s1.append(i)

        s2 = []
        for i in t:
            if i == "#":
                if s2:
                    s2.pop()
            else:
                s2.append(i)

        return s1 == s2
        