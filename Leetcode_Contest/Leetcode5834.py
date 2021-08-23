class Solution(object):
    def minTimeToType(self, word):
        """
        :type word: str
        :rtype: int
        """
        
        char = "a"
        sum_operation = len(word)
        for i in range(len(word)):
            c = word[i]
            m, n = max(char, c), min(char, c)
            sum_operation += min(ord(m) - ord(n), 26 - ord(m) + ord(n))
            char = c

        return sum_operation

S = Solution()
word = "abc"
prrint()