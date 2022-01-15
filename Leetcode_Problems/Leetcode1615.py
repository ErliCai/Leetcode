class Solution(object):
    def maximalNetworkRank(self, n, roads):
        """
        :type n: int
        :type roads: List[List[int]]
        :rtype: int
        """
        
        self.d = {i:set() for i in range(n)}
        for r1, r2 in roads:
            # if r1 not in self.d:
            #     self.d[r1] = set()
            self.d[r1].add(r2)
            
            # if r2 not in self.d:
            #     self.d[r2] = set()
            self.d[r2].add(r1)
            
        maximum = 0
        for i in range(n):
            for j in range(i+1, n):
                
                s = len(self.d[i]) + len(self.d[j])
                #print(i, j , s)
                if j in self.d[i]:
                    s -= 1
                maximum = max(maximum, s)
                
        return maximum