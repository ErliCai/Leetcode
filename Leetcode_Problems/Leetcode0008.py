class Solution(object):
    def myAtoi(self, s):
        """
        :type s: str
        :rtype: int
        """
        
        if not s:
            return 0
        
        s = s.strip()
        sign = 1
        if not s:
            return 0
        if s[0] == "-":
            sign = -1
            s = s[1:]
        elif s[0] == "+":
            s = s[1:]
        
        if not s:
            return 0
        
        if not 0 <= ord(s[0]) - ord("0") <= 9:
            return 0
        
        i = 0
        while i < len(s):
            if 0 <= ord(s[i]) - ord("0") <= 9:
                i += 1
            else:
                i -= 1
                break
        s = s[:i+1]
        
        print(s)
        

        num = int(s) * sign
        #print(num, 2 ** 31 - 1)
        if num >= 2 ** 31 - 1:
            num = 2 ** 31 - 1
        elif num < - 2 ** 31:
            num = - 2 ** 31
        
        return num


S = Solution()
s = "32"
print(S.myAtoi(s))