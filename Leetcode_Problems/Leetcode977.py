class Solution(object):
    def sortedSquares(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """
        
        i = 0
        while i < len(nums) and nums[i] < 0:
            i += 1
        nums.insert(i, 0)
        low = i - 1
        high = i
        nums = [i**2 for i in nums]
        
        
        result = []
        while low >= 0 and high <= len(nums) - 1:
            #print(low, high, nums)
            if nums[low] <= nums[high]:
                result.append(nums[low])
                low -= 1
            else:
                result.append(nums[high])
                high += 1

        #print(low, high)
        #print(result)
        if low == -1:
            result += nums[high:]
        else:

            result += nums[low::-1]
        result.pop(0)
        return result

S = Solution()
nums = [-5,-3,-2,-1]
result = S.sortedSquares(nums)
print(result)
