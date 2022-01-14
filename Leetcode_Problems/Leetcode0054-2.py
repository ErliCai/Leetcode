class Solution(object):
    def spiralOrder(self, matrix):
        """
        :type matrix: List[List[int]]
        :rtype: List[int]
        """
        
        m, n = len(matrix[0]) - 1, len(matrix) - 1

        return self.spiralRecursive(matrix, [0,0], [m, n])

    def spiralRecursive(self, matrix, start, end):



        startm, startn = start
        endm, endn = end

        if startm - endm > 0 or startn - endn > 0:
            return []

        if startm - endm == 0:

            return [matrix[i][startm]  for i in range(startn, endn+1)]

        if startn - endn == 0:

            return matrix[startn][startm: endm+1]

        print(matrix[startn][startm: endm])
        print([matrix[i][endm] for i in range(startm, endm)])
        print(matrix[endn][endm: startm: -1])
        print([matrix[i][startm] for i in range(endn, startn, -1)])

        first_part = matrix[startn][startm: endm] + [matrix[i][endm] for i in range(startn, endn)] + \
            matrix[endn][endm: startm: -1] + [matrix[i][startm] for i in range(endn, startn, -1)]

        second_part = self.spiralRecursive(matrix, [startm+1, startn+1], [endm - 1, endn - 1])

        return first_part + second_part

S = Solution()
matrix = [[1,2,3],[4,5,6],[7,8,9]]
print(S.spiralOrder(matrix))

matrix = [[1,2,3,4],[5,6,7,8],[9,10,11,12]]
print(S.spiralOrder(matrix))
