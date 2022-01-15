class Solution(object):
    def restoreIpAddresses(self, s):
        """
        :type s: str
        :rtype: List[str]
        """

        self.rst = []
        self.backtracking(s, [])
        return self.rst
        
    def backtracking(self, r, temp):

        if len(temp) == 4 and not r:
            self.rst.append( ".".join(temp))

        elif len(temp) == 4:
            pass

        else:
            if r[0] == "0":
                self.backtracking(r[1:], temp + ["0"])
            else:
                for i in range(min(3, len(r))):
                    if int(r[:i+1]) <= 255:
                        self.backtracking(r[i+1:], temp + [r[:i+1]])

                
S = Solution()
s = "0000"
print(S.restoreIpAddresses(s))
s = "25525511135"
print(S.restoreIpAddresses(s))