def checkValidity(board, new, pos):
    row, col = board[pos[0]], [r[pos[1]] for r in board]

    box = []
    r, c = pos[0]//3 * 3, pos[1]//3 * 3
    for i in range(3):
        for j in range(3):
            box.append(board[r+i][c+j])

    if new in row or new in col or new in box:
        return False

    return True

def toBeFilled(board):
    for i in range(9):
        for j in range(9):
            if board[i][j] == ".":
                return [i,j]

def solveSudoku(board):
    """
    :type board: List[List[str]]
    :rtype: None Do not return anything, modify board in-place instead.
    """
    nums = [str(i) for i in range(1,10)]
    tobefilled = toBeFilled(board)
    if tobefilled is None:
        return board
    else:
        r, c = tobefilled
    
    for i in nums:
        if checkValidity(board, i, tobefilled):
            board2 = [ele[::] for ele in board]
            board2[r][c] = i
            b = solveSudoku(board2)
            if b is not None:
                return b
            



board = [["5","3",".",".","7",".",".",".","."],["6",".",".","1","9","5",".",".","."],[".","9","8",".",".",".",".","6","."],["8",".",".",".","6",".",".",".","3"],["4",".",".","8",".","3",".",".","1"],["7",".",".",".","2",".",".",".","6"],[".","6",".",".",".",".","2","8","."],[".",".",".","4","1","9",".",".","5"],[".",".",".",".","8",".",".","7","9"]]
# print(checkValidity(board=board, new="2", pos=[0,1]))
# print(toBeFilled(board))
# board2 = [[1 for i in range(9)] for i in range(9)]
# print(toBeFilled(board2))
print(solveSudoku(board))