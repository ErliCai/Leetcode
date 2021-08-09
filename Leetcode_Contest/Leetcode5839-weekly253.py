class Solution(object):
    def minStoneSum(self, piles, k):
        """
        :type piles: List[int]
        :type k: int
        :rtype: int
        """
        


        n_piles = []
        for p in sorted(piles):
            n_piles.append(bin(p)[2:])

        largest = n_piles.pop()
        largest // 2
        return

S = Solution()
piles = [5,4,9]
k = 2
S.minStoneSum(piles, k)