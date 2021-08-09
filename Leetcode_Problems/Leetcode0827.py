from os import makedev


class Solution(object):
    def largestIsland(self, grid):
        """
        :type grid: List[List[int]]
        :rtype: int
        """
        
        n = len(grid)
        visited = [[0] * n for i in range(n)]
        directions = [[1, 0], [-1, 0], [0, 1], [0, -1]]
        #water = set()
        land = set()

        islands = []
        area = []
        for i in range(n):
            for j in range(n):
                # if grid[i][j]:
                #     land.add((i,j))
                # else:
                #     water.add((i,j))
                if grid[i][j] and not visited[i][j]:
                    island = []
                    visited[i][j] = 1
                    boundary = [[i,j]]
                    while boundary:
                        x, y = boundary.pop()
                        island.append((x,y))
                        for dx, dy in directions:
                            if 0 <= x + dx < n and 0 <= y + dy < n and not visited[x + dx][y + dy] and grid[x + dx][y + dy]:
                                visited[x + dx][y + dy] = 1
                                boundary.append([x+dx, y+dy])

                    islands.append(set(island))
                    area.append(len(island))

        land_island = {}
        for i in range(len(islands)):
            for x, y in islands[i]:
                land_island[(x, y)] = i

        max_area = 0
        for island in islands: 
            adjacent = set()
            for x, y in island:
                for dx1, dy1 in directions:
                    ad = []
                    for dx2, dy2 in directions:
                        new_x = x + dx1 + dx2
                        new_y = y + dy1 + dy2
                        if 0 <= new_x < n and 0 <= new_y < n and grid[new_x][new_y] and (new_x, new_y) not in island:
                            ad.append(land_island[(new_x, new_y)])
                    ad = set(ad)
                    adjacent.add(tuple(ad))
            for a in adjacent:
                area_curr = len(island)
                for la in a:
                    area_curr += area[la]
                max_area = max(max_area, area_curr)

        if max_area:
            return min(max_area + 1, n * n)
        else:
            if area:
                return min(max(area) + 1, n * n)
            else:
                return 1


S = Solution()
grid = [[1,1],[1,1]]
print(S.largestIsland(grid))

# a = [(1,2) , (3,4)]
# print(set(a))        

