class Solution(object):
    def merge(self, intervals):
        """
        :type intervals: List[List[int]]
        :rtype: List[List[int]]
        """

        self.intervals = sorted(intervals, key= lambda x: x[0])
        
        def mergable(interval1, interval2):
            i1, j1 = interval1
            i2, j2 = interval2

            if j1 >= i2:
                return True
            else:
                return False

        def merge(intervals):
            print(intervals)
            i = 0
            new_intervals = []
            merged = False
            while i < len(intervals) - 1:
                #print(i)
                i1, j1 = intervals[i]
                i2, j2 = intervals[i+1]
                if mergable(intervals[i], intervals[i+1]):
                    new_intervals.append([min(i1,i2), max(j1,j2)])
                    if i == len(intervals) - 3:
                        new_intervals.append(intervals[i+2])
                    i += 2
                    merged = True
                else:
                    new_intervals.append(intervals[i])
                    if i == len(intervals) - 2:
                        new_intervals.append(intervals[i+1])
                    i += 1
            self.intervals = new_intervals
            return merged

        while len(self.intervals) > 1 and merge(self.intervals):
            continue

        return self.intervals

S = Solution()
intervals = [[1,3],[2,6],[8,10],[15,18]]
print(S.merge(intervals))

        