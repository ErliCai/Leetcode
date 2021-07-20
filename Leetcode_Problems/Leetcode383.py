import collections
from typing import Collection


class Solution(object):
    def canConstruct(self, ransomNote, magazine):
        """
        :type ransomNote: str
        :type magazine: str
        :rtype: bool
        """
        
        s1 = set(ransomNote)
        dict1 = {i : ransomNote.count(i) for i in s1}
        s2 = set(magazine)
        dict2 = {i : magazine.count(i) for i in s2}

        return s1 <= s2 and not False in [dict1[c] <= dict2[c] for c in s1]

s = Solution()
ransomNote = "aab"
magazine = "baa"
print(s.canConstruct(ransomNote, magazine))
