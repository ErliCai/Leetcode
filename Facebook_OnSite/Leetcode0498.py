class Solution(object):
    def findDiagonalOrder(self, mat):
        """
        :type mat: List[List[int]]
        :rtype: List[int]
        """
        m, n = len(mat), len(mat[0]) # m, n = 3, 3
        smaller = min(m, n) # smaller = 3
        rst = []
        for i in range(m+n-1):
            if i < smaller:
                for j in range(i+1):
                    if i % 2 == 0:
                        rst.append(mat[i-j][j])
                    else:
                        rst.append(mat[j][i-j])
            elif i < m + n - 1- smaller:
                for j in range(smaller):
                    if m < n:
                        if i % 2 == 0:
                            rst.append(mat[m-1-j][i-m+j+1])
                        else:
                            rst.append(mat[j][i-j])
                    else:
                        if i % 2 == 0:
                            rst.append(mat[i-j][j])
                        else:
                            rst.append(mat[i-n+j+1][n-j-1])
            else:
                s = m + n - 1
                for j in range(m+n-1-i):
                    if i % 2 == 0:
                        rst.append(mat[m-1-j][i+1+j-m])
                    else:
                        rst.append(mat[i+1+j-n][n-1-j])
                        
        return rst