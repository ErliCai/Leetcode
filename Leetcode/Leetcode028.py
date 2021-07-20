class Solution(object):
    def strStr(self, haystack, needle):
        """
        :type haystack: str
        :type needle: str
        :rtype: int
        """
        
        if needle == "":
            return 0
        count = [0] * 26
        for c in needle:
            count[ord(c) - ord("a")] += 1

        low = high = 0
        while low < len(haystack):
            #print(low,high, count)
            if max(count) > 0:
                if high < len(haystack):
                    count[ord(haystack[high]) - ord("a")] -= 1
                    high += 1
                else:
                    return -1
            else:
                if any(count):
                    count[ord(haystack[low]) - ord("a")] += 1
                    low += 1
                else:
                    return low

class Solution2(object):
    def strStr(self, haystack, needle):
        """
        :type haystack: str
        :type needle: str
        :rtype: int
        """

        if len(needle) == 0:
            return 0
        elif len(needle) > len(haystack):
            return -1

        kmp_list = self.kmpList(needle)
        #print(kmp_list)
        i = j = 0
        while i < len(haystack):
            #print(i,j)
            if haystack[i] == needle[j]:
                i += 1
                j += 1
                if j == len(needle):
                    return i-j
            else:
                if j == 0:
                    i += 1
                else:
                    j = kmp_list[j-1]

        return -1


    def kmpList(self, str):
        l = []
        for i in range(len(str)):
            substr = str[:i+1]
            maxprefix = 0
            for j in range(len(substr)-1):
                #print(substr, j, substr[:-1-j],substr[1+j:])
                if substr[:-1-j] == substr[1+j:]:
                    maxprefix = len(substr) - 1 - j
                    break
            #print(maxprefix)
            l.append(maxprefix)
        return l



S = Solution2()
haystack = "mississippi"
needle = "issip"
print(S.strStr(haystack, needle))

# s = "aabaaf"
# print(S.kmpList(s))