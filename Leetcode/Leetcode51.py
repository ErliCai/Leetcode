class Solution(object):
    def solveNQueens(self, n):
        """
        :type n: int
        :rtype: List[List[str]]
        """
        def transform(solution):
            r = []
            for s in solution:
                row  = ["."] * n
                row[s] = "Q"
                r.append("".join(row))
            return r

        l = []
        self.backtrack(l, [], n, 0)
        l = [transform(solution) for solution in l]
        #print(transform(l[0]))
        return l

    def backtrack(self, solution, temp, n, k):
        if k == n:
            solution.append(temp)

        for i in range(n):
            if self.isvalid(temp, i):
                self.backtrack(solution, temp+[i], n, k+1)

    def isvalid(self, prev, next):

        if next in prev:
            return False
        n = len(prev)
        for i in range(n):
            if abs(next - prev[i]) == abs(n - i):
                return False
        return True


S = Solution()
n = 6
print(len(S.solveNQueens(n)))