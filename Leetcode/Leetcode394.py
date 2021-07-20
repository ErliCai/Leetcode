class Solution(object):
    def decodeString(self, s):
        """
        :type s: str
        :rtype: str
        """
        
        i = 0
        bracket = 0
        expand = False
        start , end = None, None
        while i < len(s):
            if not expand and 48<= ord(s[i]) < 58:
                length = s[i:].index("[")
                start = i = i + length + 1
                expand = True
                bracket += 1
            elif expand:
                if s[i] == "[":
                    bracket += 1
                if s[i] == "]":
                    bracket -= 1
                    if bracket == 0:
                        end = i - 1
                        break

            i += 1

        if expand:
            #print(s[:start-2] , s[start: end + 1] * int(s[start-2]) )
            return s[:start-1-length] + self.decodeString(s[start: end + 1] * int(s[start-1-length:start-1])) + self.decodeString(s[end+2:])
        else:
            return s


S = Solution()
s = "3[a]2[bc]"
a = S.decodeString(s)
print(a)
s = "3[a2[c]]"
a = S.decodeString(s)
print(a)
s = "10[leetcode]"
a = S.decodeString(s)
print(a)