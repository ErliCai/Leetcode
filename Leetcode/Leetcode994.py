class Solution(object):
    def orangesRotting(self, grid):
        """
        :type grid: List[List[int]]
        :rtype: int
        """
        
        m = len(grid)
        n = len(grid[0])

        number_orange = 0
        number_rotten = 0
        boundary = []

        for i in range(m):
            for j in range(n):
                if grid[i][j] == 1:
                    number_orange += 1
                elif grid[i][j] == 2:
                    number_orange += 1
                    number_rotten += 1
                    boundary.append([i,j])


        dirc = [[1,0], [-1,0], [0,1], [0,-1]]
        t = 0
        while boundary and number_orange != number_rotten:
            tmp_boundary = []
            for b in boundary:
                for d in dirc:
                    x , y = b[0] + d[0], b[1] + d[1]
                    if not (0 <= x < m and 0 <= y < n):
                        continue
                    
                    if grid[x][y] == 1:
                        number_rotten += 1
                        grid[x][y] = 2
                        tmp_boundary.append([x,y])
            t += 1
            #print(tmp_boundary)
            boundary = tmp_boundary

        if number_rotten != number_orange:
            return -1
        else:
            return t


S = Solution()
grid = [[2,1,1],[1,1,0],[0,1,1]]
print(S.orangesRotting(grid))