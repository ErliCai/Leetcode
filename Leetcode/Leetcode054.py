class Solution(object):
    def spiralOrder(self, matrix):
        """
        :type matrix: List[List[int]]
        :rtype: List[int]
        """
        
        m = len(matrix)
        n = len(matrix[0])

        if m == 1:
            return matrix[0]
        elif m == 2:
            return matrix[0] + matrix[1][::-1]

        elif n == 1:
            return [matrix[i][0] for i in range(m)]
        elif n == 2:
            return [matrix[0][0]] + [matrix[i][1] for i in range(m-1)] + [matrix[m-1][1]] + [matrix[i+1][0] for i in range(m-1)][::-1]

        else:
            l = (matrix[0][:-1] + [matrix[i][n-1] for i in range(m-1)] + 
                matrix[m-1][1:][::-1] + [matrix[i+1][0] for i in range(m-1)][::-1])

            print(matrix)

            inner = [[0] * (n-2) for i in range(m-2)]
            for i in range(m-2):
                for j in range(n-2):
                    print(i,j)
                    c = matrix[i+1][j+1]
                    inner[i][j] = matrix[i+1][j+1]

            r = self.spiralOrder(inner)

            return l + r
        

        

S = Solution()
# m = [[1,2,3],[1,2,3]]
# print(S.spiralOrder(m))

# m2 = [[1,2],[1,2],[1,2]]
# print(S.spiralOrder(m2))

m3 = [[1,2,3,4],[5,6,7,8],[9,10,11,12]]
print(S.spiralOrder(m3))