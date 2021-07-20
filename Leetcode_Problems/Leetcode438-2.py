class Solution(object):
    def findAnagrams(self, s, p):
        """
        :type s: str
        :type p: str
        :rtype: List[int]
        """
        if len(s) < len(p):
            return []

        answer = []

        freqList = [0] * 26
        for i in range(len(p)):
            freqList[ord(p[i]) - ord("a")] += 1
            freqList[ord(s[i]) - ord("a")] -= 1

        if not all(freqList):
            answer.append(0)

        for i in range(len(s) - len(p)):
            freqList[ord(s[i]) - ord("a")] += 1
            freqList[ord(s[i+len(p)]) - ord("a")] -= 1
            if not any(freqList):
                answer.append(i+1)

        return answer

S = Solution()
s = "cbaebabacd"
p = "abc"
print(S.findAnagrams(s,p))


