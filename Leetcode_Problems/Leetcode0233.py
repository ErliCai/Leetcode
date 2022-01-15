
class Solution(object):
    def countDigitOne(self, n):
        """
        :type n: int
        :rtype: int
        """
        
        cnt = 0
        
        mul = 1
        l = 0
        while n > 0:
            print("iter")
            r, n = n % 10, n // 10
            cnt += n * mul
            print(cnt)
            if r == 1:
                cnt += (l + 1)
            elif r > 1:
                cnt += mul
            print(cnt)

            l += mul * r
            mul *= 10

        print(cnt)
        return cnt

S = Solution()
n = 25
S.countDigitOne(n)