class Solution(object):
    def maxAreaOfIsland(self, grid):
        """
        :type grid: List[List[int]]
        :rtype: int
        """
        
        m = len(grid)
        n = len(grid[0])
        direc = ((0,1), (0,-1), (1,0), (-1,0))
        
        max_area = 0
        for i in range(m):
            for j in range(n):
                if grid[i][j] == 1:
                    area = 0
                    q = [(i,j)]
                    grid[i][j] = 0
                    while q:
                        x, y = q.pop()
                        for d in direc:
                            dx, dy = d
                            if 0 <= x + dx < m and 0 <= y + dy < n and grid[x+dx][y+dy] == 1:
                                q.append((x+dx, y+dy))
                                grid[x+dx][y+dy] = 0

                        area += 1

                    max_area = max(area , max_area)

        return max_area