class Solution(object):
    def smallestStringWithSwaps(self, s, pairs):
        """
        :type s: str
        :type pairs: List[List[int]]
        :rtype: str
        """
        
        swapable = {}
        for p in pairs:
            p1, p2 = p

            if not p1 in swapable:
                swapable[p1] = set()
            if not p2 in swapable:
                swapable[p2] = set()
            swapable[p1].add(p2)
            swapable[p2].add(p1)

        covered = set()
        swapset_list = []
        for c in swapable:
            if c in covered:
                continue
            else:
                return
