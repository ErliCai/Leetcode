class Solution(object):
    def kthSmallest(self, matrix, k):
        """
        :type matrix: List[List[int]]
        :type k: int
        :rtype: int
        """

        n = len(matrix)
        visited = [[[0] * n ] * n]
        direction = [[0,1], [1,0]]
        d = dict()
        d[matrix[0][0]] = [(0,0)]
        while k > 0:
            min_v = min(d)

            i, j = d[min_v].pop()
            for x,y in direction:
                if x + i < n and y + j < n:
                    if visited[x+i][y+j] == 0:
                        return
            if not d[min_v]:
                d.pop(min_v)