class Solution(object):
    def numIslands(self, grid):
        """
        :type grid: List[List[str]]
        :rtype: int
        """
        
        m, n = len(grid), len(grid[0])

        islands = 0
        d = [(1,0), (-1,0), (0,1), (0,-1)]
        for i in range(m):
            for j in range(n):
                if grid[i][j] == "1":
                    islands += 1
                    front = [(i,j)]
                    grid[i][j] = "-1"
                    while front:
                        x, y = front.pop()
                        for dx, dy in d:
                            new_x, new_y = x+dx, y+dy
                            if 0 <= new_x < m and 0 <= new_y < n and grid[new_x][new_y] == "1":
                                grid[new_x][new_y] = "-1"
                                front += [(new_x,new_y)]
            
        return islands



class Solution2(object):
    def numIslands(self, grid):
        """
        :type grid: List[List[str]]
        :rtype: int
        """
        
        m, n = len(grid), len(grid[0])
        self.count = sum([1 for i in range(m) for j in range(n) if grid[i][j] == "1"])
        self.id = [i for i in range(m * n)]

        def find(x):
            if self.id[x] != x:
                return find(self.id[x])
            else:
                return x

        def union(a, b):
            a_id, b_id = find(a), find(b)
            if a_id < b_id:
                self.id[b_id] = a_id
                self.count -= 1
            elif a_id > b_id:
                self.id[a_id] = b_id
                self.count -= 1

        dirctions = [(1,0), (0,1)]
        for i in range(m):
            for j in range(n):
                if grid[i][j] == "1":
                    for dx, dy in dirctions:
                        x , y= i+dx, j+dy
                        if 0 <= x < m and 0 <= y < n and grid[x][y] == "1":
                            union(i*n + j, x*n + y)


        return self.count
                


        
[["1","1","1","1","1","0","1","1","1","1"],
["1","0","1","0","1","1","1","1","1","1"],
["0","1","1","1","0","1","1","1","1","1"],
["1","1","0","1","1","0","0","0","0","1"],
["1","0","1","0","1","0","0","1","0","1"],
["1","0","0","1","1","1","0","1","0","0"],
["0","0","1","0","0","1","1","1","1","0"],
["1","0","1","1","1","0","0","1","1","1"],
["1","1","1","1","1","1","1","1","0","1"],
["1","0","1","1","1","1","1","1","1","0"]]