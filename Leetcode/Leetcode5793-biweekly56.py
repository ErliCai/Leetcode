class Solution(object):
    def nearestExit(self, maze, entrance):
        """
        :type maze: List[List[str]]
        :type entrance: List[int]
        :rtype: int
        """
        m = len(maze)
        n = len(maze[0])
        maze[entrance[0]][entrance[1]] = 0
        direc = [[0,1], [0,-1], [1,0], [-1, 0]]
        toBeExpolored = [entrance]

        steps = 1
        while toBeExpolored:
            #print(toBeExpolored)
            next_Iter = []
            for cell in toBeExpolored:
                i,j = cell[0], cell[1]

                for d in direc:
                    dx,dy = d[0], d[1]

                    x, y = i+dx, j+dy
                    
                    if 0<= x < m and 0 <= y < n and maze[x][y] == "." :
                        #print(x, y , maze[x][y])
                        if (x == 0 or x == m-1 or y == 0 or y == n-1) and [x,y] != entrance:
                            return steps
                        maze[x][y] = 0
                        next_Iter.append([x,y])
                        #print("iter", next_Iter)

            toBeExpolored = next_Iter
            steps += 1
        return -1


S = Solution()
# maze = [["+","+",".","+"],[".",".",".","+"],["+","+","+","."]]
# entrance = [1,2]
# a = S.nearestExit(maze, entrance)
# print(a)


# maze = [["+","+","+"],[".",".","."],["+","+","+"]] 
# entrance = [1,0]
# a = S.nearestExit(maze, entrance)
# print(a)

# maze = [[".","+"]]
# entrance = [0,0]
# a = S.nearestExit(maze, entrance)
# print(a)

import numpy
maze = [[".",".",".",".",".","+",".",".","."],[".","+",".",".",".",".",".",".","."],[".",".","+",".","+",".","+",".","+"],[".",".",".",".","+",".",".",".","."],[".",".",".",".","+","+",".",".","."],["+",".",".",".",".",".",".",".","."],[".",".",".","+",".",".",".",".","."],[".",".",".","+",".",".",".",".","+"],["+",".",".","+",".","+","+",".","."]]
e = numpy.array(maze)
print(e)
entrance = [8,4]
a = S.nearestExit(maze, entrance)
print(a)

e = numpy.array(maze)
print(e)