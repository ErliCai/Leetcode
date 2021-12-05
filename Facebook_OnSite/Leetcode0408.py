class Solution(object):
    def validWordAbbreviation(self, word, abbr):
        """
        :type word: str
        :type abbr: str
        :rtype: bool
        """

        return self.recursion(word, abbr)
    
    def recursion(self, word, abbr):
        if not abbr and not word:
            return True
        elif not abbr or not word:
            return False
        if abbr[0].isalpha():
            if abbr[0] == word[0]:
                return self.recursion(word[1:], abbr[1:])
            else:
                return False
        else:
            i = 0
            while i < len(abbr):
                i += 1
                if i == len(abbr) or not abbr[i].isnumeric():
                    break
            if len(word) < int(abbr[:i]) or abbr[:i][0] == "0":
                return False
            return self.recursion(word[int(abbr[:i]):], abbr[i:])
                

S = Solution()
# word = "internationalization"
# abbr = "i12iz4n"
# print(S.validWordAbbreviation(word, abbr))

word = "internationalization"
abbr = "i5a11o1"
print(S.validWordAbbreviation(word, abbr))