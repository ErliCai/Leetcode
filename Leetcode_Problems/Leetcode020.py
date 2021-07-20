
class Solution(object):
    def isValid(self, s):
        """
        :type s: str
        :rtype: bool
        """
        parenthesis = "([{}])"

        stack = []
        for c in s:
            if parenthesis.index(c) < 3:
                stack.append(c)
            else:
                if not stack or parenthesis.index(stack[-1]) + parenthesis.index(c) != 5:
                    return False
                else:
                    stack.pop()
                
        if not stack:
            return True
        return False

S = Solution()
s = "()"
print(S.isValid(s))