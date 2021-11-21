class Solution(object):
    def merge(self, intervals):
        """
        :type intervals: List[List[int]]
        :rtype: List[List[int]]
        """

        rst = []
        for i in intervals:
            if not rst:
                rst.append(i)
            else:
                if rst[-1][1] >= i[0]:
                    rst[-1][1] = i[1]
                else:
                    rst.append(i)

        return rst

S = Solution()
intervals = [[1,3],[2,6],[8,10],[15,18]]
print(S.merge(intervals))
intervals = [[1,4],[4,5]]
print(S.merge(intervals))