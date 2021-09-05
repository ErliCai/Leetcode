class Solution(object):
    '''
    This solution will TLE
    '''
    def updateMatrix(self, mat):
        """
        :type mat: List[List[int]]
        :rtype: List[List[int]]
        """
        
        m, n = len(mat), len(mat[0])

        def BFS(p):
            x, y = p
            if mat[x][y] == 0:
                return 0
            for distance in range(1, max(m,n)):
                directions = ([(distance - i, i) for i in range(distance)] 
                    + [(distance - i, -i) for i in range(distance)]
                    + [(-distance + i, i) for i in range(distance)] 
                    + [(-distance + i, -i) for i in range(distance)]
                             + [(0, distance), (0, -distance)] )
                #print(p ,directions)
                for dx, dy in directions:
                    newx, newy = x+dx, y+dy
                    if 0 <= newx < m  and 0 <= newy < n and mat[newx][newy] == 0:
                        return distance

        ans = [[[0] for i in range(n)] for j in range(m)]
        for i in range(m):
            for j in range(n):
                ans[i][j] = BFS([i,j])
        return ans


class Solution2(object):
    def updateMatrix(self, mat):
        """
        :type mat: List[List[int]]
        :rtype: List[List[int]]
        """
        
        m, n = len(mat), len(mat[0])

        ans = [[None for i in range(n)] for j in range(m)]
        fronts = []
        directions = [(0,1),(0,-1),(1,0),(-1,0)]
        for i in range(m):
            for j in range(n):
                if mat[i][j] == 0:
                    ans[i][j] = 0
                    fronts.append((i,j))
        distance = 1
        while fronts:
            new_fronts = []
            for x, y in fronts:
                for dx, dy in directions:
                    newx, newy = x+dx, y+dy
                    if 0 <= newx < m and 0 <= newy < n and ans[newx][newy] == None:
                        new_fronts.append((newx, newy))
                        ans[newx][newy] = distance
            distance += 1
            fronts = new_fronts
        

        return ans

S = Solution2()
mat = [[0,0,0],[0,1,0],[0,0,0]]
mat = [[0,0,0],[0,1,0],[1,1,1]]
print(S.updateMatrix(mat))