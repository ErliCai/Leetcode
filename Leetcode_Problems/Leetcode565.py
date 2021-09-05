class Solution(object):
    def arrayNesting(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        
        length = [0] * len(nums)

        for i in range(len(nums)):
            if not length[i]:
                l = [nums[i]]
                s = set(l)
                l = [i] + l
                while nums[l[-1]] not in s:
                    s.add(nums[l[-1]])
                    l.append(nums[l[-1]])
                    
                n = nums[l[-1]]
                loop = False
                for j in range(len(l)):
                    if l[j] != n and not loop:
                        length[l[j]] = len(l) - j - 1
                    elif l[j] == n:
                        loop = True
                        k = len(l) - j - 1
                        length[l[j]] = k
                    else:
                        length[l[j]] = k

        print(length)
        n = max(length)
        if n == 0:
            return 1
        return n + 1

S = Solution()
nums = [1,2,3,0]
nums = [5,4,0,3,1,6,2]
nums = [0,1,2,3,4]
print(S.arrayNesting(nums))