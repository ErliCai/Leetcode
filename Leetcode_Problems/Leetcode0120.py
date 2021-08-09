class Solution(object):
    def minimumTotal(self, triangle):
        """
        :type triangle: List[List[int]]
        :rtype: int
        """

        v = [triangle[0][0]]
        for i in range(1, triangle):
            last_row, new_row = v, triangle[i]

            new_row[0] = new_row[0] + last_row[0]
            new_row[-1] = new_row[-1] + last_row[-1]
            for j in range(1, len(new_row) - 1):
                new_row[j] = new_row[j] + max(last_row[j], last_row[j-1])

            v = new_row

        return min(new_row)
