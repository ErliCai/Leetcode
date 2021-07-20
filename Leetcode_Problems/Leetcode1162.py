class Solution(object):
    def maxDistance(self, grid):
        """
        :type grid: List[List[int]]
        :rtype: int
        """
        
        n = len(grid)

        land = []
        for i in range(n):
            for j in range(n):
                if grid[i][j] == 1:
                    land.append([i,j])

        if len(land) == 0 or len(land) == n*n:
            return -1

        boundary = land

        t = -1
        dirc = [[1,0], [-1,0], [0,1], [0,-1]]
        while boundary:
            tmp = []
            for b in boundary:
                i, j = b
                for d in dirc:
                    x, y = d

                    if (0 <= x + i < n and 0 <= y + j < n):
                        if grid[x+i][y+j] == 0:
                            grid[x+i][y+j] = 1
                            tmp.append([x+i, y+j])

            boundary = tmp
            t += 1

        return t

S = Solution()
grid = [[1,0,1],[0,0,0],[1,0,1]]
print(S.maxDistance(grid))
grid = [[1,0,0],[0,0,0],[0,0,0]]
print(S.maxDistance(grid))