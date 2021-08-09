class Solution(object):
    def reverseParentheses(self, s):
        """
        :type s: str
        :rtype: str
        """
        
        stacks = [[]]
        
        for i in range(len(s)):


            if s[i] == "(":
                stacks.append([])
            elif s[i] == ")":
                stack = stacks.pop()
                stacks[-1] += stack[::-1]
            else:
                stacks[-1].append(s[i])

        return "".join(stacks[0])


S = Solution()
s = "(abcd)"
print(S.reverseParentheses(s))