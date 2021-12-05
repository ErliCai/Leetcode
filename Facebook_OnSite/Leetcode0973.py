from random import *

class Solution(object):
    def kClosest(self, points, k):
        """
        :type points: List[List[int]]
        :type k: int
        :rtype: List[List[int]]
        """
        distances = [(self.distance_square(p), p) for p in points]
        print(self.partition(distances, k))
        return [i[1] for i in self.partition(distances, k)]

    def distance_square(self, point):
        x, y = point
        return x ** 2 + y ** 2

    def partition(self, distances_point, k):

        smaller = []
        larger = []

        i = int(random() * len(distances_point))
        pivot = distances_point[i]

        for d, p in distances_point:
            if d > pivot[0]:
                larger.append((d,p))
            else:
                smaller.append((d,p))

        if len(smaller) == k:
            return smaller
        elif len(smaller) < k:
            return self.partition(larger, k-len(smaller)) + smaller
        else:
            return self.partition(smaller, k)


S = Solution()
points = [[1,3],[-2,2]]
k = 1
print(S.kClosest(points=points, k = k))