class Solution(object):
    def lengthOfLongestSubstring(self, s):
        """
        :type s: str
        :rtype: int
        """
        
        i, j = 0, 0
        chars = set()
        max_len = 0

        while j < len(s):
            #print(chars)
            if s[j] in chars:
                chars.remove(s[i])
                i += 1
            else:
                chars.add(s[j])
                j += 1
                max_len = max(max_len, j - i)
                
        return max_len