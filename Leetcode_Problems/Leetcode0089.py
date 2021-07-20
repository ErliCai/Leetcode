class Solution(object):
    def grayCode(self, n):
        """
        :type n: int
        :rtype: List[int]
        """
        num_set = {i for i in range(1,2 ** n)}
        print(num_set)
        return self.backtrack([0], num_set, 0)

    def backtrack(self, temp, rnum, last):
        print(rnum)
        if not rnum:
            return temp
        
        else:
            for n in rnum:
                if self.valid(abs(last - n)):
                    r_copy = rnum.copy()
                    r_copy.remove(n)
                    return self.backtrack(temp + [n], r_copy, n)

    def valid(self, n):

        if n == 1:
            return True
        for i in range(16):
            if n == 2 ** i:
                return True
        return False

S = Solution()
n = 2
print(S.grayCode(n))