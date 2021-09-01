class Solution(object):
    def isValidSudoku(self, board):
        """
        :type board: List[List[str]]
        :rtype: bool
        """
        
        def validrow(row):
            row = board[row]
            num_list = [i for i in row if i != "."]
            num_set = set(num_list)
            return len(num_list) == len(num_set)

        def validcolumn(column):
            column = [board[i][column] for i in range(9)]
            #print(column)
            num_list = [i for i in column if i != "."]
            num_set = set(num_list)
            return len(num_list) == len(num_set)

        def validsquare(pos):
            nums = []
            x , y = pos
            for i in range(3):
                for j in range(3):
                    if board[i + x][j + y] != ".":
                        nums.append(board[i + x][j + y])
            nums_set = set(nums)
            #print(nums, nums_set)
            return len(nums_set) == len(nums)

        positions = [(3*i, 3*j) for i in range(3) for j in range(3)]
        #print(positions)

        row_validity = all([validrow(i) for i in range(9)])
        column_validity = all([validcolumn(i) for i in range(9)])
        square_validity = all([validsquare(p) for p in positions])

        #print(row_validity, column_validity, square_validity)

        return row_validity and column_validity and square_validity

S = Solution()
board = [["5","3",".",".","7",".",".",".","."]
,["6",".",".","1","9","5",".",".","."]
,[".","9","8",".",".",".",".","6","."]
,["8",".",".",".","6",".",".",".","3"]
,["4",".",".","8",".","3",".",".","1"]
,["7",".",".",".","2",".",".",".","6"]
,[".","6",".",".",".",".","2","8","."]
,[".",".",".","4","1","9",".",".","5"]
,[".",".",".",".","8",".",".","7","9"]]

S.isValidSudoku(board)