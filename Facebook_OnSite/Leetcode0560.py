class Solution(object):
    def subarraySum(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: int
        """
        running_sums = []
        sum = 0
        for i in nums:
            sum += i
            running_sums.append(sum)

        cnt = 0
        for i in range(len(nums)):
            if running_sums[i] == k:
                cnt += 1
            for j in range(i+1,len(nums)):
                if running_sums[j] - running_sums[i] == k:
                    cnt += 1

        return cnt


class Solution(object):
    def subarraySum(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: int
        """

        running_sums = {0:1}
        sum = 0
        cnt = 0
        for i in nums:
            sum += i
            if sum not in running_sums:
                running_sums[sum] = 0
            running_sums[sum] += 1
            if sum - k in running_sums:
                cnt += running_sums[sum-k]

        return cnt
        