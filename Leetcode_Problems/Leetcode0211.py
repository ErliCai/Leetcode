from collections import defaultdict

class WordDictionary(object):

    def __init__(self):
        """
        Initialize your data structure here.
        """
        self.d = dict()

    def addWord(self, word):
        """
        :type word: str
        :rtype: None
        """
        d = self.d
        for w in word:
            if w in d:
                d = d[w]
            else:
                d[w] = dict()

        d[" "] = 1
        

    def search(self, word):
        """
        :type word: str
        :rtype: bool
        """
        possible_path = [self.d]
        for w in word:
            tmp_path = []
            if w == ".":
                for path in possible_path:
                    for c in path:
                        tmp_path.append(path[c])
            else:
                for path in possible_path:
                    if w in path:
                        tmp_path.append(path[w])

            possible_path = tmp_path
            
        for path in possible_path:
            if " " in path:
                return True

        return False
            


a = {u'a': {' ': 1, u'd': {}}, ' ': 1, u'b': {}, u'm': {}, u'd': {u'a': {}, ' ': 1, u'd': {}}}
print(a["a"])