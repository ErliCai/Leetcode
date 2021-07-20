# class Solution(object):
#     def longestValidParentheses(self, s):
#         """
#         :type s: str
#         :rtype: int
#         """
        
#         i = 0
#         j = 0
#         result = 0
#         prev = False
#         while i < len(s):
#             if not prev:
#                 stack = []
#                 l = 0
#                 prev = True

#             if stack:
#                 if stack[-1] == "(" and s[i] == ")":
#                     l += 2
#                     stack.pop()
#                 elif s[i] == "(":
#                     stack.append("(")
#                 elif stack[-1] == ")" and s[i] == "(":
#                     result = max(result, l)
#                     prev = False
#                     j = i
#             else:
#                 if s[i] == "(":
#                     stack.append("(")
#                 else:
#                     prev = False
#                     j = i
#                     result = max(result, l)
#             #print(i, l)
#             i += 1
        
#         last_piece = s[j:]
        

#         return result








class Solution(object):
    def longestValidParentheses(self, s):
        """
        :type s: str
        :rtype: int
        """
        
        i = 0
        j = 0
        result = 0
        prev = False
        while i < len(s):
            if not prev:
                stack = []
                l = 0
                prev = True

            if stack:
                if stack[-1] == "(" and s[i] == ")":
                    l += 2
                    stack.pop()
                elif s[i] == "(":
                    stack.append("(")
                elif stack[-1] == ")" and s[i] == "(":
                    result = max(result, l)
                    prev = False
                    j = i
            else:
                if s[i] == "(":
                    stack.append("(")
                else:
                    prev = False
                    j = i
                    result = max(result, l)
            #print(i, l)
            i += 1
        
        last_piece = s[j:]
        

        return result
so = Solution()
s = "()(()"
print(so.longestValidParentheses(s))
print()
s = "(()"
print(so.longestValidParentheses(s))
print()
s = ")()())"
print(so.longestValidParentheses(s))