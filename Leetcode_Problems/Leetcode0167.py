class Solution(object):
    def twoSum(self, numbers, target):
        """
        :type numbers: List[int]
        :type target: int
        :rtype: List[int]
        """
        
        i, j = 0, len(numbers) - 1
        while i < j:
            num1, num2 = numbers[i], numbers[j]
            if num1 + num2 < target:
                i += 1
            elif num1 + num2 > target:
                j -= 1
            else:
                return i, j