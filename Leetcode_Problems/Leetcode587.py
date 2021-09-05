class Solution(object):
    def outerTrees(self, trees):
        """
        :type trees: List[List[int]]
        :rtype: List[List[int]]
        """
        
        if len(trees) <= 3:
            return trees

        def dist(p1, p2):
            import math
            return math.sqrt((p1[0] - p2[0])^2 + (p1[1] - p2[1])^2)

        def cross_product(l1, l2):

            return abs((l1[0] - l2[0]) * (l1[1] - l2[1]))

        def cal_angle(prev, curr, next):
            d1 = dist(prev, curr)
            d2 = dist(curr, next)
            x1, x2, y1, y2 = prev[0] - curr[0], next[0] - curr[0], prev[1] - curr[1], next[1] - curr[1]

            return (x2 * y1 - x1 * y2) / (d1 * d2)

        ans = []

        left_most = min(trees, key = lambda x : x[0])
        left_most_points = [x for x in trees if x[0] == left_most[0]]
        ans += left_most_points
        if len(left_most_points) > 1:
            lh, ll = max(left_most_points, key = lambda x : x[0]), min(left_most_points, key = lambda x : x[0])
        else:
            lh = left_most_points[0]
            ll = [lh[0], lh[1] - 1]
        
        return left_most_points

S = Solution()
points = [[1,1],[1,2], [2,2],[2,0],[2,4],[3,3],[4,2]]
print(S.outerTrees(points))