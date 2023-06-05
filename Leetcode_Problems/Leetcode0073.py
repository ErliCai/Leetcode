class Solution(object):
    def setZeroes(self, matrix):
        """
        :type matrix: List[List[int]]
        :rtype: None Do not return anything, modify matrix in-place instead.
        """
        
        rows = []
        for i in range(len(matrix)):
            if 0 in matrix[i]:
                rows.append(True)
            else:
                rows.append(False)

        cols = []
        for i in range(len(matrix[0])):
            if 0 in [matrix[j][i] for j in range(len(matrix))]:
                cols.append(True)
            else:
                cols.append(False)

        for i in range(len(matrix)):
            for j in range(len(matrix[0])):
                if rows[i] == 0 or cols[j] == 0:
                    matrix[i][j] = 0
        
