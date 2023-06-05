class Solution(object):
    def myAtoi(self, s):
        """
        :type s: str
        :rtype: int
        """
        
        s = s.strip()
        if not s:
            return 0
        sign = 1
        if s[0] == "+":
            s = s[1:]
        elif s[0] == "-":
            sign = -1
            s = s[1:]
            
        if not s:
            return 0

        if not s[0].isnumeric():
            return 0
        i = 0
        while i < len(s) and s[i].isnumeric():
            i += 1

        rst = sign * int(s[:i])

        if rst > 2 ** 31 - 1:
            return 2 ** 31 - 1
        elif rst < - 2 ** 31:
            return - 2 ** 31

        return rst