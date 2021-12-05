class Solution(object):
    def findBuildings(self, heights):
        """
        :type heights: List[int]
        :rtype: List[int]
        """
        
        ocean_views = []
        for i in range(len(heights)):
            
            h = heights[i]
            if not ocean_views or heights[ocean_views[-1]] > h:
                ocean_views.append(i)
            else:
                while ocean_views and heights[ocean_views[-1]] < h:
                    ocean_views.pop()
                ocean_views.append(i)

        return ocean_views

S = Solution()
heights = [4,2,3,1]
print(S.findBuildings(heights))