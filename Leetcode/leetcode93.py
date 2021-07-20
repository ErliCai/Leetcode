class Solution(object):
    def restoreIpAddresses(self, s):
        """
        :type s: str
        :rtype: List[str]
        """
        return self.restoreHelper(s, 4)

    def restoreHelper(self, s, r):
        if len(s) > 3 * r or len(s) < r:
            return None
        if r == 1 and self.valid(s):
            return [s]

        n = min(3, len(s))
        possibleIp = []
        for i in range(n):
            if self.valid(s[:i+1]):
                next_pieces = self.restoreHelper(s[i + 1:], r - 1)
                if next_pieces:
                    for n in next_pieces:
                        possibleIp.append(s[:i + 1] + "." + n)

        return possibleIp

    def valid(self, s):
        if s == "0":
            return True
        elif s[0] == "0":
            return False
        elif int(s) <= 255:
            return True
        else:
            return False


S = Solution()
s = "25525511135"
a = S.restoreIpAddresses(s)
print(a)
s = "010010"
a = S.restoreIpAddresses(s)
print(a)