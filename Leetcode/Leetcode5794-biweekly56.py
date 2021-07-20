class Solution(object):
    def sumGame(self, num):
        """
        :type num: str
        :rtype: bool
        """

        sum_first, qmark_first = self.sum(num,0)
        sum_second, qmark_second = self.sum(num,1)
        n_qmark = qmark_first + qmark_second
        if n_qmark % 2 == 1:
            return True

        if qmark_first >= qmark_second:
            #print(qmark_first, qmark_second)
            q = qmark_first - qmark_second 
            if sum_second - sum_first == (9 * q) / 2:
                return False
        else:
            q = qmark_second - qmark_first
            if sum_first - sum_second == (9 * q) / 2:
                return False

        return True

    def sum(self, num, half):
        n = len(num)
        if half:
            num = num[(n+1)//2:]
        else:
            num = num[:(n+1)//2]

        sum = 0
        n_qmark = 0
        for i in num:
            if i != "?":
                sum += int(i)
            else:
                n_qmark += 1
        return sum, n_qmark




S = Solution()
num = "5023"
print(S.sumGame(num))

num = "25??"
print(S.sumGame(num))

num = "?3295???"
print(S.sumGame(num))