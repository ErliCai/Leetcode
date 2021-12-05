class Solution(object):
    def groupStrings(self, strings):
        """
        :type strings: List[str]
        :rtype: List[List[str]]
        """

        def compare(a, b):
            if len(a) != len(b):
                return False
            diff = (ord(a[0]) - ord(b[0])) % 26
            for i in range(len(a)):
                if (ord(a[i]) - ord(b[i])) % 26 != diff:
                    return False

            return True

        rst = []
        rst.append([strings[0]])

        for i in range(1,len(strings)):
            found = False
            for r in rst:
                if compare(r[0], strings[i]):
                    r.append(strings[i])
                    found = True
                    break

            if not found:
                rst.append([strings[i]])

        return rst

S = Solution()
strings = ["abc","bcd","acef","xyz","az","ba","a","z"]
S.groupStrings(strings)