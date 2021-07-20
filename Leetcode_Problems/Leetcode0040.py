class Solution(object):
    def combinationSum2(self, candidates, target):
        """
        :type candidates: List[int]
        :type target: int
        :rtype: List[List[int]]
        """

        candidates.sort()
        l = []
        self.backtrack(l, candidates, target, [])
        return l


    def backtrack(self, accumulator, candidate, target, temp):

        if target == 0:
            accumulator.append(temp)
        for i in range(len(candidate)):
            ci = candidate[i]
            if i != 0 and candidate[i] == candidate[i-1]:
                continue
            if ci <= target:
                self.backtrack(accumulator, candidate[i+1:], target - ci, temp + [ci])
            else:
                break

S = Solution()
candidates = [10,1,2,7,6,1,5]
target = 8
a = S.combinationSum2(candidates, target)
print(a)