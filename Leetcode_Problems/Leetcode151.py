class Solution(object):
    def reverseWords(self, s):
        """
        :type s: str
        :rtype: str
        """
        
        wordlist = s.split(" ")
        wordlist = [word for word in wordlist if word is not ""]
        wordlist = wordlist[::-1]

        return " ".join(wordlist)


S = Solution()
s = "  hello world  "
print(S.reverseWords(s))