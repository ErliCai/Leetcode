class Solution(object):
    def numberOfCombinations(self, num):
        if num[0] == "0":
            return 0
        else:
            return self.numberOfCombinations_helper("0", num) + 1

    def numberOfCombinations_helper(self, last, num):
        """
        :type num: str
        :rtype: int
        """

        if not num or num[0] == "0":
            return 0
        else:
            if int(num) > int(last):
                i = 1
                while int(last) > int(num[:i]) and i <= len(num):
                    i += 1
                #print(last, num, i)
                ans_l = [self.numberOfCombinations_helper(num[:j], num[j:]) for j in range(i, len(num) - 1)]
                #print(num, ans_l)
                return sum(ans_l) % (10 ** 9 + 7)
            else:
                return 0
        
S = Solution()
num = "327"
# num = "094"
# num = "9999999999999"
print(S.numberOfCombinations(num))
                