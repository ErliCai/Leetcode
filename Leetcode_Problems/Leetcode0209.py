

class Solution(object):
    def minSubArrayLen(self, target, nums):
        """
        :type target: int
        :type nums: List[int]
        :rtype: int
        """
        length, start, end, sum = 0, 0, 0, 0
        nums.append(0)

        while end < len(nums):
            if target > sum:
                sum += nums[end]
                end += 1
            else:
                if length == 0 or end - start <= length:
                    length = end - start
                sum -= nums[start]
                start += 1
   
        return length

S = Solution()
target = 7
nums = [2,3,1,2,4,3]
print(S.minSubArrayLen(target, nums))