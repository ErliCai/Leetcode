class Solution(object):
    def longestWord(self, words):
        """
        :type words: List[str]
        :rtype: str
        """
        
        word_length = {}
        for word in words:
            n = len(word)
            if n not in word_length:
                word_length[n] = set()
            word_length[n].add(word)

        valid = set(word_length[1])
        n = max(word_length)
        for i in range(2, n +1):
            new_valid = set()
            for word in word_length[n]:
                if word[:-1] in valid:
                    new_valid.add(word)

            if not new_valid:
                return sorted(list(valid))[0]
            else:
                valid = new_valid


        return sorted(list(valid))[0]