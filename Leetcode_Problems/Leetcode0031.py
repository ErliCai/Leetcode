class Solution(object):
    def nextPermutation(self, nums):
        """
        :type nums: List[int]
        :rtype: None Do not return anything, modify nums in-place instead.
        """

        length = len(nums)
        if length != 1:
            largest = True
            for i in range(length-1):
                curr = nums[-1-i]
                next = nums[-2-i]

                if curr > next:
                    largest = False
                    subnums = [num for num in nums[-1-i:] if num > next]
                    m = min(subnums)
                    j = nums[-1-i:].index(m)
                    nums[-2-i], nums[-1-i+j] = nums[-1-i+j], nums[-2-i]
                    s = nums[-1-i:]
                    s.sort()


                    for j in range(1+i):
                        nums[-1-j] = s[-1-j]
                    return 
            if largest:
                nums.sort()
                return 




a = [1,2,3]
s = Solution()
s.nextPermutation(a)
print(a)
s.nextPermutation(a)
print(a)