class Solution(object):
    def numSquares(self, n):
        """
        :type n: int
        :rtype: int
        """
        
        
        base = 0
        while  base * base <= n:
            base += 1

        squares = {i * i for i in range(1, base)}
        print(squares)

        nMinusSquares = {n}
        count = 0
        while 0 not in nMinusSquares:
            newSet = set()
            for i in nMinusSquares:
                s = {i - square for square in squares if i >= square}
                newSet = newSet.union(s)
            nMinusSquares = newSet
            count += 1

        print(count)
        return count



        


S = Solution()
n = 12
print(S.numSquares(n))