class Solution(object):
    def recoverArray(self, n, sums):
        """
        :type n: int
        :type sums: List[int]
        :rtype: List[int]
        """
        
        potential_nums = []
        original_sums = sums[::]
        while len(sums) >= 2:
            sums.sort()
            i = int(len(sums) / 2)
            potential_nums.append(sums[i] - sums[0])
            sums = sums[i:]

        def finding(temp, remaining):
            if not remaining:
                return temp
            else:
                r = remaining[0]
                Y = True
                for t in temp:
                    if t + r not in original_sums:
                        Y = False
                print(temp, r, Y)
                if Y:
                    finding(temp + [r], remaining[1:])
                finding(temp + [-r], remaining[1:])
                
        return finding([], potential_nums)


S = Solution()
n = 3
sums = [-3,-2,-1,0,0,1,2,3]
print(S.recoverArray(n, sums))