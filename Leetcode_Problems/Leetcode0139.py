class Solution(object):

    def __init__(self):
        self.mem = []
        self.max_len = 20

    def wordBreak(self, s, wordDict):
        """
        :type s: str
        :type wordDict: List[str]
        :rtype: bool
        """
        self.mem = [False] * (1 + len(s))
        self.mem[0] = True
        self.word_set = set(wordDict)
        self.wordBreak_dp(s)

        return self.mem[-1]

    def wordBreak_dp(self, s):
        for i in range(1, 1+ len(s)):
            for j in range(1, self.max_len):
                if i-j >=0 and s[i-j:i] in self.word_set and self.mem[i-j]:
                    self.mem[i] = True

                    

        