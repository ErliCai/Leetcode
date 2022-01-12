class Solution(object):
    def numIslands(self, grid):
        """
        :type grid: List[List[str]]
        :rtype: int
        """
        
        m, n = len(grid), len(grid[0])

        visited = [[0 for i in range(n)] for i in range(m)]
        directions = ((0,1), (0,-1), (1,0), (-1,0))

        cnt = 0
        for i in range(m):
            for j in range(n):

                if not visited[i][j] and grid[i][j] == "1":
                    cnt += 1
                    # deepth first search for each island
                    q = [(i,j)]
                    visited[i][j] = 1
                    while q:
                        x, y = q.pop()
                        print(x,y)
                        for dx, dy in directions:
                            if 0 <= x+dx < m and 0 <= y+dy < n and not visited[x+dx][y+dy] and grid[i][j] == "1" :
                                q.append((x+dx, y+dy))
                                visited[x+dx][y+dy] = 1
                            
                    

        return cnt