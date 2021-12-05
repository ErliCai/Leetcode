class Solution(object):
    def isToeplitzMatrix(self, matrix):
        """
        :type matrix: List[List[int]]
        :rtype: bool
        """
        
        m, n = len(matrix), len(matrix[0])

        if m < n:
            for i in range(m):
                element = matrix[i][0]
                for j in range(m-i):
                    if matrix[i+j][j] != element:
                        return False
            for i in range(n):
                element = matrix[0][i]
                for j in range(min(m, n-i)):
                    if matrix[j][i+j] != element:
                        return False


        return True