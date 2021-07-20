class Solution(object):
    def countCharacters(self, words, chars):
        """
        :type words: List[str]
        :type chars: str
        :rtype: int
        """
        def word_freq(word):
            word_freq = [0] * 26
            for i in range(26):
                word_freq[i] = word.count(chr(ord("a") + i))

            return word_freq

        char_f = word_freq(chars)

        count = 0
        for word in words:
            word_f = word_freq(word)
            covered = True
            for i in range(26):
                if word_f[i] > char_f[i]:
                    covered = False

            if covered:
                count += len(word)

        return count


class Solution2(object):
    def countCharacters(self, words, chars):
        """
        :type words: List[str]
        :type chars: str
        :rtype: int
        """

        count = 0
        d = {chars.count(chr(ord("a") + i)) for i in range(26)}

        for word in words:
            covered = True
            for w in word:
                if not covered:
                    break
                if word.count(w) > d[w]:
                    covered = False

            if covered:
                count += len(word)

        return count


