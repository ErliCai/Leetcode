class Solution(object):
    def minRemoveToMakeValid(self, s):
        """
        :type s: str
        :rtype: str
        """
        return self.removeInvalidLeft(self.removeInvalidRight(s))
        
    def removeInvalidRight(self, s):
        
        new_string = ""
        count_brackets = 0
        for i in s:
            if i == "(":
                count_brackets += 1
                new_string += i
            elif i == ")":
                count_brackets -= 1
                if count_brackets < 0:
                    count_brackets = 0
                else:
                    new_string += i
            else:
                count_brackets += s

        return new_string

    def removeInvalidLeft(self, s):
        count_brackets = 0
        left_brackets = 0
        for i in s:
            if i == "(":
                count_brackets += 1
                left_brackets += 1
            elif i == ")":
                count_brackets -= 1
        if count_brackets == 0:
            return S
        else:
            new_string = ""
            cnt = 0
            for char in s:
                if char != "(":
                    new_string += char
                else:
                    if cnt < left_brackets - count_brackets:
                        new_string += char
                        cnt += 1
            return new_string


S = Solution()
s = "()))()))"
print(S.removeInvalidRight(s))





class Solution(object):
    def minRemoveToMakeValid(self, s):
        """
        :type s: str
        :rtype: str
        """

        s = list(s)
        stack = []

        for i in range(len(s)):
            if s[i] == "(":
                stack.append(i)
            elif s[i] == ")":
                if stack:
                    stack.pop()
                else:
                    s[i] = ""
        for left_brackets in stack:
            s[left_brackets] = ""

        return "".join(s)