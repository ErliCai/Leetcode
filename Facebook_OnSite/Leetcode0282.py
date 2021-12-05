class Solution(object):
    def addOperators(self, num, target):
        """
        :type num: str
        :type target: int
        :rtype: List[str]
        """

        self.rst = []
        self.backtrack(None, target, None, num, None)
        print(self.rst)
        return self.rst
    
    def backtrack(self, cur, target, last, remaining, expr):

        if len(remaining) == 0 and cur == target:
            self.rst.append(expr)
        else:
            for i in range(len(remaining)):
                if remaining[0] != "0" or i == 0:
                    num = int(remaining[:i+1])
                    if cur is None:
                        self.backtrack(num, target, num, remaining[i+1:], str(num))
                    else:
                        if last is not None:
                            self.backtrack(cur - last + last * num, target, last * num, remaining[i+1:], expr + "*" + str(num))
                        self.backtrack(cur + num, target, num, remaining[i+1:], expr + "+" + str(num))
                        self.backtrack(cur - num, target, -num, remaining[i+1:], expr + "-" + str(num))


S = Solution()
num = "00"
target = 0
S.addOperators(num, target)