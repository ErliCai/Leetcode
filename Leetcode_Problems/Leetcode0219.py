class Solution(object):
    def containsNearbyDuplicate(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: bool
        """

        d = dict()
        for i in nums[:k]:
            if i not in d:
                d[i] = 0
            d[i] += 1

        for v in d.values():
            if v >= 2:
                return True

        for i in range(len(nums) - k):
            d[nums[i]] -= 1
            if nums[k+i-1] not in d:
                d[nums[k+i-1]] = 0
            d[nums[k + i - 1]] += 1
            if d[nums[k+i-1]] > 1:
                return True

        return False


