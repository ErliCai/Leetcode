class Solution(object):
    def searchRange(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[int]
        """
        

        if not nums:
            return [-1, -1]

        low = 0
        high = len(nums) - 1
        
        while low <= high:
            print(low, high, nums, target)
            mid = (low + high) // 2

            if nums[mid] < target:
                low = mid + 1
            elif nums[mid] > target:
                high = mid -1
            else:
                # print("searching")
                # print(low, mid, high)
                l = self.searchRange(nums[low:mid], target)
                r = self.searchRange(nums[mid+1:high+1], target)
                # print(l,nums[low:mid])
                # print(r,nums[mid+1:high+1])
                if l[0] != -1:
                    lbound = low + l[0]
                else:
                    lbound = mid
                if r[1] != -1:
                    rbound = r[1]+1+mid
                else:
                    rbound = mid
                print(lbound, rbound)
                return [lbound, rbound]

        return [-1,-1]

S = Solution()
nums = [5,7,7,8,8,10]
target = 8
result =S.searchRange(nums, target)
print(result)