class Solution(object):
    def canBeTypedWords(self, text, brokenLetters):
        """
        :type text: str
        :type brokenLetters: str
        :rtype: int
        """
        
        count = 0
        word_list = text.split()
        b_set = set(brokenLetters)
        for w in word_list:
            w_set = set(w)

            if not w_set.intersection(b_set):
                count += 1

        return count