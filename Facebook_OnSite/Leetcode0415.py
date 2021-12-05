class Solution(object):
    def addStrings(self, num1, num2):
        """
        :type num1: str
        :type num2: str
        :rtype: str
        """

        return self.addRecursive_nocarry(num1, num2)
        
    def addRecursive_nocarry(self, num1, num2):

        if not num1:
            return num2
        if not num2:
            return num1

        ld1 = int(num1[-1])
        ld2 = int(num2[-1])
        if ld1 + ld2 < 10:
            return self.addRecursive_nocarry(num1[:-1], num2[:-1]) + str(ld1+ ld2)
        else:
            return self.addRecursive_carry(num1[:-1], num2[:-1]) + str(ld1+ ld2)[1]

    def addRecursive_carry(self, num1, num2):
        if not num1:
            return self.addRecursive_nocarry(num2, "1")
        if not num2:
            return self.addRecursive_nocarry(num1, "1")

        ld1 = int(num1[-1])
        ld2 = int(num2[-1])
        if ld1 + ld2 + 1 < 10:
            return self.addRecursive_nocarry(num1[:-1], num2[:-1]) + str(ld1+ ld2+ 1)
        else:
            return self.addRecursive_carry(num1[:-1], num2[:-1]) + str(ld1+ ld2+1)[1]

S = Solution()
num1 = "11"
num2 = "123"
print(S.addStrings(num1, num2))