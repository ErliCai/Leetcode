class Solution(object):
    def minCostClimbingStairs(self, cost):
        """
        :type cost: List[int]
        :rtype: int
        """
        
        length = len(cost)
        l = [0] * length

        l[0] = cost[0]
        l[1] = cost[1]
        for i in range(2, length):
            l[i] = cost[i] + min(l[i-1], l[i-2])
            
        #print(l)

        return min(l[-1], l[-2])