class Solution(object):
    def canJump(self, nums):
        """
        :type nums: List[int]
        :rtype: bool
        """
        
        if 0 not in nums:
            return True
        
        table = [False] * len(nums)
        table[0] = True

        for i in range(len(nums)):
            #print(table)
            if table[-1]:
                return True
            if not table[i]:
                return False
            else:
                for j in range(nums[i]+1):
                    if i + j < len(nums):
                        table[i+j] = True

        return True



class Solution2(object):
    def canJump(self, nums):
        """
        :type nums: List[int]
        :rtype: bool
        """

        max_dist = 1
        length = len(nums)
        i = 1
        while max_dist < nums:
            if max_dist < i:
                return False
            else:
                max_dist = max(max_dist, nums[i] + i)

            i += 1

        return True