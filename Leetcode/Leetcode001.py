class Solution(object):
    def twoSum(self, nums, target):
        
        numsdic = {}
        for i in range(len(nums)):
            if nums[i] in numsdic:
                return [i, numsdic[nums[i]]]
            else:
                numsdic[target-nums[i]] = i