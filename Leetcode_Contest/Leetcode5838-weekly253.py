class Solution(object):
    def isPrefixString(self, s, words):
        """
        :type s: str
        :type words: List[str]
        :rtype: bool
        """
        
        count = 0
        length = len(s)

        for word in words:
            l = len(word)

            if s[count: count + l] != word:
                return False
            count += l

            if len(s) == count:
                return True
            if len(s) < count:
                return False
