class Solution(object):
    def wordPattern(self, pattern, s):
        """
        :type pattern: str
        :type s: str
        :rtype: bool
        """
        
        d = {}
        word_set = set()
        s = s.split()
        
        if len(s) != len(pattern):
            return False
        
        for i in range(len(pattern)):
            if pattern[i] not in d:
                if s[i] in word_set:
                    return False
                word_set.add(s[i])
                d[pattern[i]] = s[i]
            else:
                if s[i] != d[pattern[i]]:
                    return False

        return True