class Solution(object):
    def checkSubarraySum(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: bool
        """
        if len(nums) == 1:
            return False

        # csm for continuous sum mod k
        csm = set()

        sum = 0
        for index in nums:
            i = nums[index]
            sum = (sum + i) % k
            if sum in csm or sum == 0:
                if not(nums[index] == 0 and nums[index-1] != 0):
                    return True
            csm.add(sum)

        return False


class Solution(object):
    def checkSubarraySum(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: bool
        """

        sum = 0
        cms = set()
        for i in range(len(nums)):
            num = nums[i]
            sum = (sum + num) % k

            if sum == 0 or sum in cms:
                if num % k != 0 or (nums[i-1] % k == 0 and i != 0):
                    return True

            cms.add(sum)

        return False