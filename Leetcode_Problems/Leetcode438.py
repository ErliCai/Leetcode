class Solution(object):
    def findAnagrams(self, s, p):
        """
        :type s: str
        :type p: str
        :rtype: List[int]
        """
        answer = []
        for i in range(len(s) - len(p) + 1):
            subs = s[i:i+len(p)]
            if self.subDic(self.toDic(p), self.toDic(subs)):
                answer.append(i)

        return answer


    def toDic(self, str):
        r = {}
        for c in str:
            if c in r:
                r[c] += 1
            else:
                r[c] = 1
        return r

    def subDic(self, dic1, dic2):
        
        keyCheck = dic1.keys() <= dic2.keys()
        if not keyCheck:
            return keyCheck
        freqCheck = True
        for key in dic1:
            if dic1[key] > dic2[key]:
                freqCheck = False

        return freqCheck

S = Solution()
s = "abab"
p = "ab"
print(S.findAnagrams(s,p))


print(all([1,2,3]))
print(all([0,0]))