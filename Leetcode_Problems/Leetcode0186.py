class Solution(object):
    def reverseWords(self, s):
        """
        :type s: List[str]
        :rtype: None Do not return anything, modify s in-place instead.
        """
        
        s = list(s)
        i, j = 0, len(s) - 1

        def reverse(s, i, j):
            while i < j:
                s[i], s[j] = s[j], s[i]
                i += 1
                j -= 1

        reverse(s, i, j)

        start = end = i = 0
        while i < len(s):
            if s[i].isalnum():
                i += 1
            elif s[i] == " ":
                end = i-1
                reverse(s, start, end)
                start = i + 1
        
        return "".join(s)
