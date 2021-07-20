
class Solution(object):
    def isAnagram(self, s, t):
        """
        :type s: str
        :type t: str
        :rtype: bool
        """
        
        dict1 = dict()
        for c in s:
            if c in dict:
                dict1[c] += 1
            else:
                dict1[c] = 1

        dict2 = dict()
        for c in s:
            if c in dict:
                dict2[c] += 1
            else:
                dict2[c] = 1 
        
        return dict1 == dict2