class Solution(object):
    def isAlienSorted(self, words, order):
        """
        :type words: List[str]
        :type order: str
        :rtype: bool
        """
        
        order_dict = {}
        for i in range(len(order)):
            order_dict[order[i]] = i

        earth_words = []
        for w in words:
            e = [chr(ord("a") + order_dict[c]) for c in w]
            earth_words.append(e)

        for i in range(len(earth_words) - 1):
            if earth_words[i] > earth_words[i+1]:
                return  False

        return True