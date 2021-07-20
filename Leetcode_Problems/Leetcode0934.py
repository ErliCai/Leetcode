class Solution(object):
    def shortestBridge(self, grid):
        """
        :type grid: List[List[int]]
        :rtype: int
        """
        length = len(grid)
        find = False
        for i in range(length):
            for j in range(length):
                if grid[i][j] == 1:
                    x, y = i, j
                    find = True
                if find:
                    break
                    
        island = []
        q = [[x,y]]
        grid[x][y] = -1
        dirction = [[0,1], [0,-1],[1,0],[-1,0]]
        while q:
            x, y = q.pop()
            island.append([x,y])
            for dx, dy in dirction:
                nx = dx + x 
                ny = dy + y
                if (0 <= nx < length and 0 <= ny < length 
                    and grid[nx][ny] == 1):
                    grid[nx][ny] = -1
                    q.append([nx,ny])
            
        
        length = len(grid)
        for i,j in island:
            grid[i][j] = -1

        i = 0
        bound = island

        while True:
            b2 = []
            for b in bound:
                for d in [[0,1], [0,-1], [1,0], [-1,0]]:
                    x = b[0] + d[0]
                    y = b[1] + d[1]
                    if 0 <= x < length and 0 <= y < length:
                        if grid[x][y] == 1:
                            return i
                        elif grid[x][y] == 0:
                            grid[x][y] = -1
                            b2.append([x,y])
            bound = b2
            i += 1


S = Solution()
grid = [[1,1,1,1,1],[1,0,0,0,1],[1,0,1,0,1],[1,0,0,0,1],[1,1,1,1,1]]
length = S.shortestBridge(grid)
print(length)