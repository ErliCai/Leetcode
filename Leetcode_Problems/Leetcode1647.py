class Solution(object):
    def minDeletions(self, s):
        """
        :type s: str
        :rtype: int
        """
        d = {}
        for c in s:
            if c not in d:
                d[c] = 0 
            d[c] += 1

        freq = list(d.values())

        occupied = set()
        cnt = 0
        for i in range(len(freq)):

            while freq[i] in occupied:
                freq[i] -= 1
                cnt += 1
            occupied.add(freq[i])

        return cnt