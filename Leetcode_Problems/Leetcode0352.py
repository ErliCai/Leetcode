class SummaryRanges(object):

    def __init__(self):
        self.ranges = []
        

    def addNum(self, val):
        """
        :type val: int
        :rtype: None
        """

        if not self.ranges:
            self.ranges.append([val,val])
            return
        for i in range(len(self.ranges)):
            if self.ranges[i][0] <= val <= self.ranges[i][1]:
                return

            if self.ranges[i][0] > val:
                self.ranges.insert(i, [val,val])
                return

            if self.ranges[i][1] == val - 1:
                if i != len(self.ranges) - 1 and self.ranges[i+1][0] == val + 1:
                    l, h = self.ranges.pop(i+1)
                    self.ranges[i][1] = h
                else:
                    self.ranges[i][1] = val
                return
            if self.ranges[i][0] == val + 1:
                self.ranges[i][0] = val
                return
        self.ranges.append([val, val])
        

    def getIntervals(self):
        """
        :rtype: List[List[int]]
        """
        
        return self.ranges