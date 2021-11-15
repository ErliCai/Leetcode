class Solution(object):
    def __init__(self):
        self.mem = []
        self.max_len = 20

    def wordBreak(self, s, wordDict):
        """
        :type s: str
        :type wordDict: List[str]
        :rtype: List[str]
        """
        self.mem = [None] * (1 + len(s))
        self.mem[0] = [""]
        self.word_set = set(wordDict)
        self.wordBreak_dp(s)

        if self.mem[-1] is not None:
            self.mem[-1] = [s[1:] for s in self.mem[-1]]

            return self.mem[-1]
        else:
            return None

    def wordBreak_dp(self, s):
        for i in range(1, 1+ len(s)):
            l = []
            for j in range(1, self.max_len):
                if i-j >=0 and s[i-j:i] in self.word_set and self.mem[i-j] is not None:
                    l += [sentense + " " + s[i-j:i] for sentense in self.mem[i-j]]
                    
            if l != []:
                self.mem[i] = l

S = Solution()
s ="catsanddog"
wordDict = ["cat","cats","and","sand","dog"]
print(S.wordBreak(s,wordDict))