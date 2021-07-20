
from collections import deque
class Solution(object):
    def removeDuplicates(self, s):
        """
        :type s: str
        :rtype: str
        """
        
        stack = deque()
        
        for c in s:
            if len(stack) > 0 and stack[-1] == c:
                stack.pop()
                
            else:
                stack.append(c)
                
        return "".join(stack)               


        
S = Solution()
s = "abbaca"
a = S.removeDuplicates(s)
print(a)