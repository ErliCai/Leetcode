class Solution(object):
    def splitIntoFibonacci(self, num):
        """
        :type num: str
        :rtype: List[int]
        """

        l = []
        self.backtrack(l, num, 1, [])

        if l:
            return l[0]
        return l        
        
    def backtrack(self, accumulator, num, k, temp):

        if not num and k > 3:
            accumulator.append(temp)

        if k <= 2:
            for i in range(len(num)):
                if self.isvalid(num[:i+1]):
                    self.backtrack(accumulator, num[i+1:], k+1, temp + [int(num[:i+1])])
        else:
            f1, f2 = temp[-1], temp[-2]
            for i in range(len(num)):
                if self.isvalid(num[:i+1]) and int(num[:i+1]) == f1 + f2:
                    self.backtrack(accumulator, num[i+1:], k+1, temp + [int(num[:i+1])])


    def isvalid(self, s):

        if s == "0" or s[0] != "0" and int(s) < 2 ** 31:
            return True
        else:
            return False

S = Solution()
num = "123456579"
print(S.splitIntoFibonacci(num))