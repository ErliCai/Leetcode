class Solution(object):
    def updateBoard(self, board, click):
        """
        :type board: List[List[str]]
        :type click: List[int]
        :rtype: List[List[str]]
        """

        m = len(board)
        n = len(board[0])
        
        i, j = click
        if board[i][j] == 'M':
                board[i][j] = "X"
                return board

        tobeRevealed = [click]
        dirc = [[1,0],[-1,0],[0,1],[0,-1],[1,1],[-1,1],[1,-1],[-1,-1]]
        while tobeRevealed:
            #print(tobeRevealed)
            tobeRevealed_nextround = []
            for c in tobeRevealed:
                noBomb = True
                bomb = 0
                i, j = c
                tmp = []
                for d in dirc:
                    x, y = d
                    if 0 <= x+i < m and 0 <= y+j < n:
                        if board[i+x][j+y] == 'M':
                            noBomb = False
                            #print([i+x,j+y])
                            bomb += 1
                        elif board[i+x][j+y] == 'E':
                            tmp.append([i+x,j+y])
                            board[i+x][j+y] = 'T'
                if noBomb:
                    tobeRevealed_nextround += tmp
                    board[i][j] = 'B'
                else:
                    for t in tmp:
                        board[t[0]][t[1]] = 'E'
                    #print(i,j,bomb)
                    board[i][j] = str(bomb)
            tobeRevealed = tobeRevealed_nextround

        return board

S = Solution()
board = [["E","E","E","E","E"],["E","E","M","E","E"],["E","E","E","E","E"],["E","E","E","E","E"]]
click = [3,0]
print(S.updateBoard(board,click))


