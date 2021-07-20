class Solution(object):
    def fourSumCount(self, nums1, nums2, nums3, nums4):
        """
        :type nums1: List[int]
        :type nums2: List[int]
        :type nums3: List[int]
        :type nums4: List[int]
        :rtype: int
        """
        
        dic = {}
        for i in nums1:
            for j in nums2:
                if (i+j) in dic:
                   dic[i+j] += 1
                else:
                    dic[i+j] = 1

        count = 0
        for i in nums3:
            for j in nums4:
                if (-i-j) in dic:
                    count += dic[-i-j]

        return count

nums1 = [1,2]
nums2 = [-2,-1]
nums3 = [-1,2]
nums4 = [0,2]
S = Solution()
print(S.fourSumCount(nums1, nums2, nums3, nums4))