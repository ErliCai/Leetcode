class Solution(object):
    def minimizeTheDifference(self, mat, target):
        """
        :type mat: List[List[int]]
        :type target: int
        :rtype: int
        """
        
        m, n = len(mat), len(mat[0])
        diff = set([target])


        for i in range(m):
            if max(diff) >= 0:
                new_diff = set()
                for partial_target in diff:
                    for j in range(n):
                        new_diff.add(partial_target - mat[i][j])
                diff = new_diff
            else:
                m = max(diff)
                diff = set([m - min(mat[i])])


        return abs(min(new_diff, key=lambda x: abs(x)))