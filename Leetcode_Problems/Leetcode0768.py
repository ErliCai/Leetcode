class Solution(object):
    def maxChunksToSorted(self, arr):
        """
        :type arr: List[int]
        :rtype: int
        """
        
        sorted_arr = sorted(arr)

        maximum = 0
        max_list = []
        for i in arr:
            maximum = max(maximum, i)
            max_list.append(maximum)

        minimum = float('inf')
        min_list = []
        for i in arr[::-1]:
            minimum = min(minimum, i)
            min_list.append(minimum)
        min_list = min_list[::-1]

        cnt = 1
        for i in range(len(max_list) - 1):
            if max_list[i] <= min_list[i+1]:
                cnt += 1
        return cnt

S = Solution()
arr = [5,4,3,2,1]
S.maxChunksToSorted(arr)

arr = [2,1,3,4,4]
S.maxChunksToSorted(arr)