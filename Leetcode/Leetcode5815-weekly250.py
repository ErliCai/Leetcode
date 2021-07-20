class Solution(object):
    def maxPoints(self, points):
        """
        :type points: List[List[int]]
        :rtype: int
        """
        n = len(points[0])
        scores = [0] * n

        for row in points:
            scores = self.dp(scores, row, n)
            print(scores)
        
        return max(scores)

    def dp(self, last, new, n):
        
        dp = []
        relavent = self.relavent(last)
        relavent_new = self.relavent(new)
        print("r    ", relavent_new)
        for i in relavent_new:
            possible_scores = [new[i] + last[j] - abs(i-j) for j in relavent]
            print("p   ",possible_scores)
            dp.append(max(possible_scores))
        return dp

    def relavent(self, row):
        max_index = 0
        relavent = []

        for i in range(len(row)):
            if row[i] - row[max_index] + (i-max_index) >= 0:
                relavent.append(i)
                max_index = i

        return relavent

[[0,3,0,4,2],[5,4,2,4,1],[5,0,0,5,1],[2,0,1,0,3]]