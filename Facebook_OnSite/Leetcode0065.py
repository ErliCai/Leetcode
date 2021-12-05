class Solution(object):
    def isNumber(self, s):
        """
        :type s: str
        :rtype: bool
        """

        if not "e" in s and not "E" in s:
            return self.isInteger(s) or self.isDecimal(s)

        if "e" in s:
            s = s.split("e")
        elif "E" in s:
            s = s.split("E")
        
        if len(s) != 2:
            return False
        return (self.isDecimal(s[0]) or self.isInteger(s[0])) and self.isInteger(s[1])


    def isDecimal(self, s):
        if not s:
            return False
        if s[0] == "+" or s[0] == "-":
            s = s[1:]

        s = s.split(".")
        if len(s) != 2:
            return False
        if not s[0] and not s[1]:
            return False
        
        return (all([self.isdigit(char) for char in s[0]]) 
            and all([self.isdigit(char) for char in s[1]]))

    def isInteger(self, s):
        if len(s) == 0:
            return False
        if s[0] == "-" or s[0] == "+":
            s = s[1:]
        return  all([self.isdigit(char) for char in s]) and len(s) != 0

    def isdigit(self, s):
        return 0 <= ord(s) - ord("0") <= 9

S = Solution()
l = ["2", "0089", "-0.1", "+3.14", "4.", "-.9", "2e10", "-90E3", "3e+7", "+6e-1", "53.5e93", "-123.456e789"]
for i in l:
    print(S.isNumber(i)) 
print()
l = ["abc", "1a", "1e", "e3", "99e2.5", "--6", "-+3", "95a54e53", ".", "4e+"]
for i in l:
    print(S.isNumber(i)) 