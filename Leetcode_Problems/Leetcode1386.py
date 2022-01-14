class Solution(object):
    def maxNumberOfFamilies(self, n, reservedSeats):
        """
        :type n: int
        :type reservedSeats: List[List[int]]
        :rtype: int
        """
        

        rows = {}
        for seat in reservedSeats:
            if seat[0] not in rows:
                rows[seat[0]] = []
            rows[seat[0]].append(seat[1])

        cnt = 2 * (n - len(rows))
        for row_num, row in rows.items():
            next_row = False
            if 1 not in row and 2 not in row and 3 not in row and 4 not in row:
                cnt += 1
                next_row = True
            if 5 not in row and 6 not in row and 7 not in row and 8 not in row:
                cnt += 1
                next_row = True
            if not next_row:
                if 5 not in row and 6 not in row and 3 not in row and 4 not in row:
                    cnt += 1

        return cnt