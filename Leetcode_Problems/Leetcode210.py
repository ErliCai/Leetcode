from collections import defaultdict

class Solution(object):
    def findOrder(self, numCourses, prerequisites):
        """
        :type numCourses: int
        :type prerequisites: List[List[int]]
        :rtype: List[int]
        """
        d1 = defaultdict(list)
        for p in prerequisites:
            d1[p[0]].append(p[1])

        d2 = defaultdict(list)
        for p in prerequisites:
            d2[p[1]].append(p[0])

        set1 = set(d1.keys)
        set2 = set(d1.values)

        for 

        visited = set()
        for k in d1:
            if k not in visited:
                visited.add(k)
                visited_thisround = {k}
                q = [k]
                while q:
                    c = q.pop()
                    next_c = d1[c]
                    prev_c = d2[c]
                    if next_c in visited_thisround or prev_c in visited_thisround:
                        return []
