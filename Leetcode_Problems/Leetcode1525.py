class Solution(object):
    def numSplits(self, s):
        """
        :type s: str
        :rtype: int
        """
        DistinctCharL = []
        chars = set()
        cnt = 0
        for i in range(len(s)-1):
            c = s[i]
            if c not in chars:
                chars.add(c)
                cnt += 1

            DistinctCharL.append(cnt)

        
        DistinctCharR = []
        chars = set()
        cnt = 0
        for i in range(len(s)-1):
            c = s[-1-i]
            if c not in chars:
                chars.add(c)
                cnt += 1

            DistinctCharR.append(cnt)   
        DistinctCharR = DistinctCharR[::-1]
        
        # print(DistinctCharR)
        # print(DistinctCharL)

        rst = 0
        length = len(s)
        for i in range(len(s)-1):
            if DistinctCharL[i] == DistinctCharR[-(length-i-1)]:
                rst += 1


        return rst