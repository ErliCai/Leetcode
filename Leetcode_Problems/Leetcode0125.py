class Solution(object):
    def isPalindrome(self, s):
        """
        :type s: str
        :rtype: bool
        """
        
        low, high = 0, len(s) - 1
        s = s.lower()
        while low <= high:
            if not s[low].islower():
                low += 1
            elif not s[high].islower():
                high -= 1
            elif s[low] != s[high]:
                return False
            else:
                low += 1
                high -= 1

        return True


s = "2"
print(s[0].isnumeric())