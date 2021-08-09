class Solution(object):
    def checkMove(self, board, rMove, cMove, color):
        """
        :type board: List[List[str]]
        :type rMove: int
        :type cMove: int
        :type color: str
        :rtype: bool
        """
        
        directions = [[1,0], [-1,0], [0,1], [0,-1],
            [1, 1], [-1, 1], [1, -1], [-1, -1]]
        colors = ["B", "W"]

        for dx, dy in directions:
            new_x = rMove + dx
            new_y = cMove + dy
            if 0 <= new_x <= 7 and 0 <= new_y <= 7:
                if board[new_x][new_y] in colors and board[new_x][new_y] != color:
                    while  0 < new_x < 7 and 0 < new_y < 7:
                        new_x += dx
                        new_y += dy
                        if board[new_x][new_y] == color:
                            return True
                        elif board[new_x][new_y] == ".":
                            break


        return False