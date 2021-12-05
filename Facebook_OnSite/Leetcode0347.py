class Solution(object):
    def topKFrequent(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: List[int]
        """
        
        frequency = dict()
        for n in nums:
            if n not in frequency:
                frequency[n] = 0
            frequency[n] += 1

        l = [(num, freq) for num, freq in frequency.items()]
        return [i[0] for i in self.partition(l, k)]

    def partition(self, nums, k):

        index = len(nums) // 2
        
        larger = []
        smaller = []
        for i in range(len(nums)):
            if i != index:
                n, f = nums[i]
                if f >= nums[index][1]:
                    larger.append((n,f))
                elif f < nums[index][1]:
                    smaller.append((n,f))

        if len(larger) == k - 1:
            return larger + [nums[index]]
        elif len(larger) > k - 1:
            return self.partition(larger, k)
        else:
            return larger + [nums[index]] + self.partition(smaller, k - len(larger) - 1) 

S = Solution()
# nums = [1,1,1,2,2,3]
# k = 2
# print(S.topKFrequent(nums, k))

nums = [1,2]
k = 2
print(S.topKFrequent(nums, k))