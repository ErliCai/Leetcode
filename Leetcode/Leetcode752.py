class Solution(object):
    def openLock(self, deadends, target):
        """
        :type deadends: List[str]
        :type target: str
        :rtype: int
        """
        
        if target == "0000":
            return 0

        possible = [[[[0 for i in range(10)] for j in range(10)] for k in range(10)] for m in range(10)]
        boundary  = [[int(i) for i in list(target)]]
        
        for d in deadends:
            d = [int(i) for i in list(d)]
            x,y,z,w = d
            possible[x][y][z][w] = -1

        def pairwiseAddition(x, y):
            z = [0] * 4
            for i in range(4):
                z[i] = (x[i] + y[i]) % 10
            return z

        moves = [[1,0,0,0], [-1,0,0,0], [0,1,0,0], [0,-1,0,0], 
            [0,0,1,0], [0,0,-1,0], [0,0,0,1], [0,0,0,-1]]
        
        t = 0
        while possible[0][0][0][0] == 0 and boundary:
            tmp_bound = []
            for b in boundary:
                for m in moves:
                    #print(b,m)
                    nextpos = pairwiseAddition(b, m)
                    i,j,k,l = nextpos
                    if possible[i][j][k][l] == 0:
                        possible[i][j][k][l] = 1
                        tmp_bound.append([i,j,k,l])

            boundary = tmp_bound
            t += 1

        if possible[0][0][0][0] == 0:
            return -1
        else:
            return t

S = Solution()
deadends = ["0201","0101","0102","1212","2002"] 
target = "0202"
print(S.openLock(deadends, target))

deadends = ["8887","8889","8878","8898","8788","8988","7888","9888"]
target = "8888"
print(S.openLock(deadends, target))
