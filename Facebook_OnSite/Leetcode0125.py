class Solution(object):
    def isPalindrome(self, s):
        """
        :type s: str
        :rtype: bool
        """
        
        new_s = [char.lower() if (char.isalpha() or char.isnumeric() )else "" for char in s]
        new_s = "".join(new_s)
        return new_s == new_s[::-1]