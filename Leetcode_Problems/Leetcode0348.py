class TicTacToe(object):

    def __init__(self, n):
        """
        :type n: int
        """
        self.n = n
        self.board = [[None for i in range(n)] for j in range(n)]  
        

    def move(self, row, col, player):
        """
        :type row: int
        :type col: int
        :type player: int
        :rtype: int
        """
        self.board[row][col] = player - 1
        if self.checkWinner(row, col):
            return player
        else:
            return 0
        
    def checkWinner(self, row, col):
        return self.checkCol(col) or self.checkRow(row) or self.checkDiag(row, col)
    
    def checkRow(self, row):
        if None not in self.board[row] and (1 not in self.board[row] or 0 not in self.board[row]):
            return True

        return False

    def checkCol(self, column):
        col = [self.board[j][column] for j in range(self.n)]
        if None not in col and (1 not in col or 0 not in col):
            return True

        return False

    def checkDiag(self, row, col):
        diag = []
        if row == col:
            diag.append([self.board[i][i] for i in range(self.n)])
        if row == self.n - 1 - col:
            diag.append([self.board[self.n-1-i][i] for i in range(self.n)])

        for d in diag:
            if None not in d and (1 not in d or 0 not in d):
                return True
        return False
        

