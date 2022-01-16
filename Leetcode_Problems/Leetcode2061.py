class Solution(object):
    def numberOfCleanRooms(self, room):
        """
        :type room: List[List[int]]
        :rtype: int
        """
        
        direction = ((0,1), (1,0),(0,-1),(-1,0))
        
        m, n = len(room), len(room[0])
        cleaned = [[0 for i in range(n)] for j in range(m)]
        
        pos = (0,0,0)
        past_pos = set()
        cnt = 0
        
        while True:
            x, y, d = pos
            if not cleaned[x][y]:
                print(x,y)
                cnt += 1
                cleaned[x][y] = 1
            if pos in past_pos:
                return cnt
            past_pos.add(pos)
            dx, dy = direction[d]
            if 0 <= dx + x< m and 0 <= dy + y< n and not room[dx + x][dy + y]:
                pos = (dx+x, dy+y, d)
            else:
                pos = (x, y, (d+1)%4)

S = Solution()
room = [[0,0,0],[1,1,0],[0,0,0]]
print(S.numberOfCleanRooms(room))