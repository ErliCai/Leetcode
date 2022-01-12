class Solution(object):
    def angleClock(self, hour, minutes):
        """
        :type hour: int
        :type minutes: int
        :rtype: float
        """
        
        angle = abs((hour + minutes / 60.0) * 30 - minutes * 6)
        
        return min(angle, 360 - angle)