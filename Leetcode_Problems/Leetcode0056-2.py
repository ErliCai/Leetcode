class Solution(object):
    def merge(self, intervals):
        """
        :type intervals: List[List[int]]
        :rtype: List[List[int]]
        """
        
        intervals.sort(key = lambda x: x[0])

        rst = []
        left, right = intervals[0][0], intervals[0][1]
        for i in intervals:
            if i[0] <= right:
                right =  max(right, i[1])
            else:
                rst.append([left, right])
                left, right = i[0], i[1]

        rst.append([left, right])

        return rst
