class Solution(object):
    def countPaths(self, n, roads):
        """
        :type n: int
        :type roads: List[List[int]]
        :rtype: int
        """
        
        matrix = [[0] * n for j in range(n)]
        #print(matrix)
        for road in roads:
            l, r = road[0], road[1]
            matrix[l][r] = matrix[r][l] = road[2]

        d_time = {i:None for i in range(n)}
        d_ways = {i:0 for i in range(n)}
        d_time[0], d_ways[0] = 0, 1
        fronts = [0]
        while fronts:
            node = min(fronts, key = lambda x: d_time[x])
            fronts.remove(node)
            time, ways = d_time[node], d_ways[node]
            for i in range(n):
                if matrix[node][i]:
                    time_i = time + matrix[node][i]
                    if d_time[i] is None:
                        fronts.append(i)
                        d_time[i] = float("inf")

                    if time_i == d_time[i]:
                        d_ways[i] += d_ways[node]
                        d_time[i] = time_i
                    elif time_i < d_time[i]:
                        d_ways[i] = d_ways[node]
                        d_time[i] = time_i

        print(d_time)
        print(d_ways)
        return d_ways[n-1] % (10 ** 9 + 7)

S = Solution()
n = 7
roads = [[0,6,7],[0,1,2],[1,2,3],[1,3,3],[6,3,3],[3,5,1],[6,5,1],[2,5,1],[0,4,5],[4,6,2]]
print(S.countPaths(n, roads))

# a  = [(1,2), (0,4)]
# print(min(a, key = lambda x: x[0]))