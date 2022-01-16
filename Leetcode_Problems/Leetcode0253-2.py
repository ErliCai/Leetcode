class Solution(object):
    def minMeetingRooms(self, intervals):
        """
        :type intervals: List[List[int]]
        :rtype: int
        """
        
        i, j = 0
        min_rooms = 0
        cnt = 0
        while i < len(intervals):
            if intervals[i][0] < intervals[j][1]:
                cnt += 1
                i += 1
            else:
                cnt -= 1
                j -= 1
            min_rooms = max(min_rooms, cnt)

        return min_rooms