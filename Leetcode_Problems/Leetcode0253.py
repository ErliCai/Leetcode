from os import EX_NOTFOUND


class Solution(object):
    def minMeetingRooms(self, intervals):
        """
        :type intervals: List[List[int]]
        :rtype: int
        """
        
        start = sorted([i[0] for i in intervals])
        end = sorted([i[1] for i in intervals])

        max_num_rooms = 0
        current_rooms = 0
        while start:
            if start[0] < end[0]:
                start.pop(0)
                current_rooms += 1
                max_num_rooms = max(current_rooms, max_num_rooms)
            else:
                end.pop(0)
                current_rooms -= 1

        return max_num_rooms