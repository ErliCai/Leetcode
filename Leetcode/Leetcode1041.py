class Solution(object):
    def isRobotBounded(self, instructions):
        """
        :type instructions: str
        :rtype: bool
        """
        
        direc = [[0,1], [1,0], [0,-1], [-1,0]]

        d = 0
        pos = [0, 0]
        for i in instructions:
            if i == "L":
                d = (d - 1) % 4
            elif i == "R":
                d = (d + 1) % 4
            elif i == "G":
                pos[0] += direc[d][0]
                pos[1] += direc[d][1]
                
        if d == 0:
            return pos == [0,0]
