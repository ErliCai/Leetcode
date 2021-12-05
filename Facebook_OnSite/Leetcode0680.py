class Solution(object):
    def validPalindrome(self, s):
        """
        :type s: str
        :rtype: bool
        """
        return self.helper_func(s, False)


    def helper_func(self, s ,deleted):
        """
        :type s: str
        :rtype: bool
        """
        head, end = 0, len(s) - 1

        while head < end:
            if s[head] == s[end]:
                head += 1
                end += 1
            else:
                if deleted:
                    return False
                else:
                    return self.helper_func(s[head:end],True) or self.helper_func(s[head+1:end+1],True)

        return True
                


S = Solution()
s = "abc"
print(S.validPalindrome(s))