from collections import defaultdict
from hashlib import new
from ssl import VERIFY_X509_PARTIAL_CHAIN

class Solution(object):
    def minJumps(self, arr):
        """
        :type arr: List[int]
        :rtype: int
        """

        posToVal = {}
        valToPos = defaultdict(set)
        
        for i in range(len(arr)):
            val = arr[i]
            posToVal[i] = val
            valToPos[val].add(i)

        # BFS
        cnt = 0
        visited = set()
        level = [0]
        while level:
            if (len(arr) - 1) in level:
                return cnt
            new_level = []
            for l in level:
                
                if l - 1 >= 0 and (l + 1) not in visited:
                    visited.add(l+1)
                    new_level.append(l+1)
                if (l+1) not in visited:
                    new_level.append(l+1)
                if posToVal[l] in valToPos:
                    pointsCanJump = valToPos[posToVal[l]]
                    for p in pointsCanJump:
                        if p  not in visited:
                            visited.add(p)
                            new_level.append(l+1)
                    del valToPos[posToVal[l]]

            level = new_level