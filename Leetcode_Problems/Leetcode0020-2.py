class Solution(object):
    def isValid(self, s):
        """
        :type s: str
        :rtype: bool
        """
        
        left = ["[", "(", "{"]
        right = ["]", ")", "}"]
        stack = []
        for c in s:
            if c in left:
                stack.append(c)
            if c in right:
                if stack and right.index(c) == left.index(stack[-1]):
                    stack.pop()
                else:
                    return False
        return not stack

            