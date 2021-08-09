class Solution(object):
    def minEatingSpeed(self, piles, h):
        """
        :type piles: List[int]
        :type h: int
        :rtype: int
        """
        

        high = max(piles)
        low = 1

        while low < high:
            print(high, low)
            mid = (low + high) // 2
            print([(p-1) // mid + 1 for p in piles], mid)
            if sum([(p-1) // mid + 1 for p in piles]) <= h:
                high = mid
            else:
                low = mid + 1

        return high

S = Solution()
piles = [3,6,7,11]
h = 8
print(S.minEatingSpeed(piles, h))