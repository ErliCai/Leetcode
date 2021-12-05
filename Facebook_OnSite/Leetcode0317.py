class Solution(object):
    def shortestDistance(self, grid):
        """
        :type grid: List[List[int]]
        :rtype: int
        """
        
        m, n = len(grid), len(grid[0])

        buildings = []
        self.emptyland = dict()
        for i in range(m):
            for j in range(n):
                if grid[i][j] == 1:
                    buildings.append((i,j))
                if grid[i][j] == 0:
                    self.emptyland[(i,j)] = []
        if len(self.emptyland) == 0:
            return -1

        for b in buildings:
            self.bfs(grid, b)

        distances = [sum(distances) for land, distances in self.emptyland.items() 
            if len(distances) == len(buildings) ]

        #print(self.emptyland)
        return min(self.emptyland.values())


    def bfs(self, grid, starting_pos):
        m, n = len(grid), len(grid[0])
        d = [[1,0], [-1, 0], [0,1], [0,-1]]
        level = [starting_pos]
        visited = [[-1 for i in range(n)] for j in range(m)]
        visited[starting_pos[0]][starting_pos[1]] = 0

        distance = 1
        while level:
            new_level = []
            for x, y in level:
                for dx, dy in d:
                    new_x = x + dx
                    new_y = y + dy
                    if 0 <= new_x < m and 0 <= new_y <n and visited[new_x][new_y] == -1 and grid[new_x][new_y] == 0:
                        new_level.append((new_x, new_y))
                        visited[new_x][new_y] = distance
                        self.emptyland[(new_x, new_y)].append(distance)

            distance += 1
            level = new_level

        return visited

S = Solution()
grid = [[1,0,0]]
print(S.shortestDistance(grid))

                
