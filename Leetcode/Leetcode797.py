class Solution(object):
    def allPathsSourceTarget(self, graph):
        """
        :type graph: List[List[int]]
        :rtype: List[List[int]]
        """
        
        path = [[0]]
        last_node = len(graph) - 1

        a = []
        while path:
            path_temp = []
            for p in path:
                last = p[-1]
                for next in graph[last]:
                    if next == last_node:
                        a.append(p + [next])
                    else:
                        path_temp.append(p + [next])
            path = path_temp

        return a


S = Solution()

graph = [[4,3,1],[3,2,4],[3],[4],[]]
a = S.allPathsSourceTarget(graph)
print(a)
