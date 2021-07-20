class Solution(object):
    def generateMatrix(self, n):
        """
        :type n: int
        :rtype: List[List[int]]
        """
        
        if n == 1:
            return [[1]]
        if n == 2:
            return [[1,2],[4,3]]
        
        else:
            matrix = [[0] * n for i in range(n)]
            inner = self.generateMatrix(n-2)
            for i in range(n-1):
                matrix[0][i] = i + 1
            for i in range(n-1):
                matrix[i][n-1] = i + n
            for i in range(n-1):
                matrix[n-1][i+1] = 3*n - 3 - i
            for i in range(n-1):
                matrix[n-1-i][0] = 3*n - 3 + i + 1

            for i in range(n-2):
                for j in range(n-2):
                    matrix[1+i][1+j] = 4 * n - 4 + inner[i][j] 

        return matrix

S = Solution()
print(S.generateMatrix(3))