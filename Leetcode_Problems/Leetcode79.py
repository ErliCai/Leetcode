class Solution(object):
    def exist(self, board, word):
        """
        :type board: List[List[str]]
        :type word: str
        :rtype: bool
        """
        char = set(word)
        char_board = set()
        for i in range(len(board)):
            char_board = char_board.union(set(board[i]))

        print(char_board)
        if char - char_board:
            return False

        for i in range(len(board)):
            for j in range((len(board[0]))):
                if self.exists_from(board, word, (i, j)):
                    return True

        return False

    def exists_from(self, board, word, pos):
        x, y = pos
        if len(word) == 1 and board[x][y] == word:
            return True

        m, n = len(board), len(board[0])
        direc = ((0, 1), (0, -1), (-1, 0), (1, 0))
        if board[x][y] == word[0]:
            b_copy = [row[::] for row in board]
            b_copy[x][y] = " "
            possible_dirc = [(x + d[0], y + d[1])
                             for d in direc if 0 <= x + d[0] < m and 0 <= y + d[1] < n]
            r = False
            for p in possible_dirc:
                r = r or self.exists_from(b_copy, word[1:], p)

            return r
        return False


S = Solution()
board = [["A","B","C","E"],["S","F","C","S"],["A","D","E","E"]]
word = "ABCCED"

board = [["A","A","A","A","A","A"],["A","A","A","A","A","A"],["A","A","A","A","A","A"],["A","A","A","A","A","A"],["A","A","A","A","A","A"],["A","A","A","A","A","A"]]
word = "AAAAAAAAAAAABAA"

print(S.exist(board,word))

s1 = {1,2,5,3}
s2 = {2,3,4}
print(s1 - s2)
