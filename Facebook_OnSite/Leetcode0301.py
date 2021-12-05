class Solution(object):
    def removeInvalidParentheses(self, s):
        """
        :type s: str
        :rtype: List[str]
        """
        
        left_wrong = 0
        right_wrong = 0
        left_count = 0
        for i in s:
            if i  == "(":
                left_count += 1

            elif i == ")":
                left_count -= 1
            if left_count < 0:
                left_count = 0
                right_wrong += 1
        left_wrong = left_count
        
        print(left_wrong, right_wrong)

        self.rst = set()
        self.backtrack("", s, len(s)-left_wrong-right_wrong)
        
        if len(self.rst) == 0:
            self.rst.add("")
            
        return list(self.rst)

    def backtrack(self, temp, remaining, n):
        if len(temp) == n and self.isValid(temp):
            self.rst.add(temp)
        else:
            if len(remaining) >= n - len(temp):
                for i in range(len(remaining)):
                    self.backtrack( temp+remaining[i], remaining[i+1:], n)
        

    
    def isValid(self, s):

        left_count = 0
        for i in s:
            if i  == "(":
                left_count += 1

            elif i == ")":
                left_count -= 1

            if left_count < 0:
                return False
        if left_count > 0:
            return False

        return True


S = Solution()
# s = "()))((()"
# print(S.removeInvalidParentheses(s))
# s = "()())()"
# print(S.removeInvalidParentheses(s))
s = "(a)())()"
print(S.removeInvalidParentheses(s))