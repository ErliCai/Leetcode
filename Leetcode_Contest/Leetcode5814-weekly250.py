class Solution(object):
    def addRungs(self, rungs, dist):
        """
        :type rungs: List[int]
        :type dist: int
        :rtype: int
        """
        
        h = 0 
        count = 0
        for i in range(len(rungs)):
            missings = (rungs[i] - h - 1) // dist
            #print(missings)
            if missings > 0:
                count += missings
                
            h = rungs[i]

        return  count

S = Solution()
rungs = [3,4,6,7]
dist = 2
print(S.addRungs(rungs, dist))