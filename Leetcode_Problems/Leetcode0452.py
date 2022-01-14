class Solution(object):
    def findMinArrowShots(self, points):
        """
        :type points: List[List[int]]
        :rtype: int
        """
        
        points = sorted(points, key = lambda x: x[1])

        cnt = 1
        first_end = points[0][1]
        for p in points:
            if p[0] > first_end:
                cnt += 1
                first_end = p[1]

        return cnt
