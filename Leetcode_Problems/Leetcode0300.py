class Solution3(object):
    def lengthOfLIS(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """

        def binarySearch(l, target):
            low, high = 0, len(l) - 1
            while low < high:
                mid = (low + high) / 2
                if l[mid] < target:
                    low = mid + 1
                else:
                    high = mid
                    
            return low
        
        ans = [-float("inf")]

        for num in nums:
            if num > ans[-1]:
                ans.append(num)

            else:
                c = binarySearch(ans, num)
                #print(c, num)
                if ans[c-1]!= num:
                    ans[c] = num
                
            #print(ans)

        return len(ans) - 1




class Solution2(object):
    def lengthOfLIS(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        
        ans = [-float("inf")]

        for num in nums:
            if num > ans[-1]:
                ans.append(num)

            else:
                c = -2
                while c > -len(ans) and ans[c] > num:
                    c -= 1
                if c >= -len(ans) and ans[c] != num:
                    ans[1+c] = num
        return len(ans) - 1


class Solution1(object):
    def lengthOfLIS(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        
        length = len(nums)
        l = [1] * length

        for i in range(length):
            for j in range(i):
                if nums[j] < nums[i]:
                    l[i] = max(l[i], l[j] + 1)

        return max(l)
