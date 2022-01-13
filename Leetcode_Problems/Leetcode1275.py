class Solution(object):
    def tictactoe(self, moves):
        """
        :type moves: List[List[int]]
        :rtype: str
        """
        if len(moves) < 5:
            return "Pending"

        self.board = [[None for i in range(3) for j in range(3)]]
        for i in range(len(moves)):
            x, y = moves[i]
            self.board[x][y] = i % 2

            if i >= 5:
                if self.checkWinner():
                    if i % 2 == 0:
                        return "A"
                    else:
                        return "B"
        if len(moves) == 9:
            return "Draw"
        return 

    def checkWinner(self):
        return self.checkCol() or self.checkRow() or self.checkDiag()
    
    def checkRow(self):
        for i in range(3):
            if None not in self.board[i] and (1 not in self.board[i] or 0 not in self.board[i]):
                return True

        return False

    def checkCol(self):
        for i in range(3):
            col = [self.board[j][i] for j in range(3)]
            if None not in col and (1 not in col or 0 not in col):
                return True

        return False

    def checkDiag(self):
        diag = []

        diag.append([self.board[i][i] for i in range(3)])
        diag.append([self.board[2-i][i] for i in range(3)])

        for d in diag:
            if None not in d and (1 not in d or 0 not in d):
                return True
        return False