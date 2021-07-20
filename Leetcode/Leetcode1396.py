from collections import defaultdict
class UndergroundSystem(object):

    def __init__(self):
        self.d = defaultdict(None)
        self.p = defaultdict(None)

    def checkIn(self, id, stationName, t):
        """
        :type id: int
        :type stationName: str
        :type t: int
        :rtype: None
        """
        self.p[id] = [stationName, t]
        

    def checkOut(self, id, stationName, t):
        """
        :type id: int
        :type stationName: str
        :type t: int
        :rtype: None
        """
        start_s, start_t = self.p[id]
        self.d((start_s, stationName)).append(t - start_t)

    def getAverageTime(self, startStation, endStation):
        """
        :type startStation: str
        :type endStation: str
        :rtype: float
        """
        times = self.d[startStation][endStation] 
        print(times)
        return float(sum(times)) / len(times)
       

a = (1,2)
b = {(1,2): 2}
b = {a:2}
print(b[(1,2)])