class Solution(object):
    def canFinish(self, numCourses, prerequisites):
        """
        :type numCourses: int
        :type prerequisites: List[List[int]]
        :rtype: bool
        """
        
        d = dict()
        for p in prerequisites:
            if p[0] not in d:
                d[p[0]] = []
            d[p[0]].append(p[1])

        coruses = list(d.keys())
        check_for_loop = set(d.keys())
        

S = Solution()
numCourses = 2
prerequisites = [[1,0],[0,1]]
print(S.canFinish(numCourses, prerequisites))
print()
numCourses = 2
prerequisites = [[1,0]]
print(S.canFinish(numCourses, prerequisites))