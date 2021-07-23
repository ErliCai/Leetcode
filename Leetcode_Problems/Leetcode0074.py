class Solution(object):
    def searchMatrix(self, matrix, target):
        """
        :type matrix: List[List[int]]
        :type target: int
        :rtype: bool
        """
        
        
        first_colomn = [matrix[i][0] for i in range(len(matrix))]
        row = self.binarySearch(first_colomn, target)
        if row == -1:
            return False
        else:
            row -= 1
        found = self.binarySearch(matrix[row], target, True)

        return found


    def binarySearch(self, nums, target, findExact = False):
        
        lower = 0
        upper = len(nums) - 1

        while lower <= upper:
            mid = (lower + upper) // 2
            if nums[mid] <= target:
                lower = mid + 1
            else:
                upper = mid - 1
            if findExact:
                if nums[mid] == target:
                    return True
        if findExact:
            False
        else:
            return lower