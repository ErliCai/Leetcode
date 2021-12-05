class Solution(object):
    def wordBreak(self, s, wordDict):
        """
        :type s: str
        :type wordDict: List[str]
        :rtype: List[str]
        """
        
        l = [[] for i in range(len(s))]
        wordDict = set(wordDict)
        for i in range(len(s)):
            if s[:i+1] in wordDict:
                l[i].append(s[:1+i])
            for j in range(i):
                print(j, l[j], s[j+1:i+1])
                if l[j] != [] and s[j+1:i+1] in wordDict:
                    l[i] += [string+" "+ s[j+1:i+1] for string in l[j]]

        #print(l)
        return l[-1]


S = Solution()
s = "catsanddog"
wordDict = ["cat","cats","and","sand","dog"]
print(S.wordBreak(s,wordDict))