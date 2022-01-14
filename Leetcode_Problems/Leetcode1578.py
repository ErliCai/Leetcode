class Solution(object):
    def minCost(self, colors, neededTime):
        """
        :type colors: str
        :type neededTime: List[int]
        :rtype: int
        """
        
        t = 0
        last_index = 0
        last_color = None
        for i in range(len(colors)):
            if last_color != colors[i]:
                if last_color == None:
                    last_color = colors[i]
                else:
                    #print(last_index, i, t)
                    t += sum(neededTime[last_index:i]) - max(neededTime[last_index:i])
                    last_color = colors[i]
                    last_index = i
        #print(t, last_index, len(colors))
        
        t += sum(neededTime[last_index:len(colors)]) - max(neededTime[last_index:len(colors)])
        
        return t