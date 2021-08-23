class Solution(object):
    def maxMatrixSum(self, matrix):
        """
        :type matrix: List[List[int]]
        :rtype: int
        """
        
        n = len(matrix)
        elements = [abs(matrix[i][j]) for i in range(n) for j in range(n)]
        odd_neg = False
        for i in range(n):
            for j in range(n):
                if matrix[i][j] < 0:
                    odd_neg = not odd_neg

        if odd_neg:
            return sum(elements) - 2 * min(elements)
        else:
            return sum(elements)
