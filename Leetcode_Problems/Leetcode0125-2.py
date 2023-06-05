class Solution(object):
    def isPalindrome(self, s):
        """
        :type s: str
        :rtype: bool
        """

        i, j = 0, len(s) - 1

        while i < j:
            if s[i].isalnum() and s[j].isalnum():
                if s[i].lower() == s[j].lower():
                    i += 1
                    j -= 1
                else:
                    return False
            elif not s[i].isalpha():
                i += 1
            elif not s[j].isalpha():
                j -= 1
        return True
