class Solution(object):
    def longestPalindrome(self, s):
        """
        :type s: str
        :rtype: str
        """
        
        max_palindrom = s[0]
        palindrome = set()
        for i in range(len(s)):
            palindrome.add((i,i))
            if i != 0 and s[i] == s[i-1]:
                palindrome.add((i-1,i))
                max_palindrom = s[i-1:i+1]

        for i in range(2, len(s), 2):
            found = False
            for j in range(len(s) - i):
                if (j+1, j+i-1) in palindrome and s[j] == s[j+i]:
                    palindrome.add((j, j+i))
                    max_palindrom = s[j:j+i+1]
                    found = True
            if not found:
                break

        palindrome = set()
        found = False
        for i in range(len(s)):
            if i != 0 and s[i] == s[i-1]:
                palindrome.add((i-1,i))
                found = True
                if len(max_palindrom) == 1:
                    max_palindrom = s[i-1:i+1]
        if not found:
            return max_palindrom

        #print(palindrome)
        for i in range(3, len(s), 2):
            found = False
            for j in range(len(s) - i):
                #print(j+1, j+i-1, s[j], s[j+i])
                if (j+1, j+i-1) in palindrome and s[j] == s[j+i]:
                    palindrome.add((j, j+i))
                    if len(max_palindrom) <= i:

                        max_palindrom = s[j:j+i+1]
                    found = True
            if not found:
                break

        return max_palindrom


S = Solution()
s = "ccc"
s = "aaaa"
print(S.longestPalindrome(s))