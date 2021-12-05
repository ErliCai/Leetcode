class Solution(object):
    def canFinish(self, numCourses, prerequisites):
        """
        :type numCourses: int
        :type prerequisites: List[List[int]]
        :rtype: bool
        """
        self.d = dict()
        for p in prerequisites:
            if p[0] not in self.d:
                self.d[p[0]] = []
            self.d[p[0]].append(p[1])

        self.courses = list(self.d.keys())
        self.to_be_checked = {c : 1 for c in self.courses}
        
        for c in self.to_be_checked:
            if self.to_be_checked[c] == 1:
                #dfs here
                if not self.helper_func(set(), c):
                    return False
        return True


    def helper_func(self, prev_cours, cur):
        for c in self.d[cur]:
            if c in prev_cours:
                return False
            else:
                if c in self.to_be_checked and self.to_be_checked[c] == 1:
                    #recursion here
                    self.to_be_checked[c] = 0
                    return self.helper_func(prev_cours.union({c}), c)

        return True
        

S = Solution()
numCourses = 2
prerequisites = [[1,0],[0,1]]
print(S.canFinish(numCourses, prerequisites))
print()
numCourses = 2
prerequisites = [[1,0]]
print(S.canFinish(numCourses, prerequisites))