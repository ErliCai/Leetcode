class Solution(object):
    def maxRunTime(self, n, batteries):
        """
        :type n: int
        :type batteries: List[int]
        :rtype: int
        """
        
    def findKthLargest(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: int
        """
        
        return self.partition(nums, k)

    def partition(self, nums, k):
        index = len(nums) // 2

        larger = []
        smaller = []
        for i in range(len(nums)):
            if i != index:
                if nums[i] > nums[index]:
                    larger.append(nums[i])
                else:
                    smaller.append(nums[i])

        if len(larger) == k-1:
            return nums[index]
        elif len(larger) > k-1:
            return self.partition(larger, k)
        else:
            return self.partition(smaller, k - 1 - len(larger))




# class Solution(object):
#     def mostPoints(self, questions):
#         """
#         :type questions: List[List[int]]
#         :rtype: int
#         """
        
#         final_score  = 0
#         points = [0] * len(questions)

#         for i in range(len(questions)):

#             if i + 1 < len(questions):
#                 points[i+1] = max(points[i+1], points[i])
#             else:
#                 final_score = max(final_score, points[i])

#             p, b = questions[i]
#             if i + b + 1< len(questions):
#                 points[i+b+1] = max(points[i+b+1], p + points[i])
#             else:
#                 final_score = max(final_score, points[i] + p)

#         return final_score

# S = Solution()
# questions = [[3,2],[4,3],[4,4],[2,5]]
# #questions = [[1,1],[2,2],[3,3],[4,4],[5,5]]
# print(S.mostPoints(questions))



# class Solution(object):
#     def minMoves(self, target, maxDoubles):
#         """
#         :type target: int
#         :type maxDoubles: int
#         :rtype: int
#         """

#         if target == 1:
#             return 0

#         cnt = 0
#         while maxDoubles > 0 and target > 2:
#             print(target, cnt)
#             target, n = target // 2, target % 2
#             cnt +=1
#             cnt += n
#             maxDoubles -= 1

#         if target == 2:
#             return cnt + 1

#         return target + cnt - 1


# S = Solution()
# target = 5
# maxDoubles = 0
# # target = 10
# # maxDoubles = 4
# # target = 766972377
# # maxDoubles = 92
# print(S.minMoves(target, maxDoubles))










# class Solution(object):
#     def divideString(self, s, k, fill):
#         """
#         :type s: str
#         :type k: int
#         :type fill: str
#         :rtype: List[str]
#         """
        
#         rst = []
#         for i in range((len(s) - 1) // k + 1):
#             rst.append(s[k*i: k * (i+1)])

#         rst[-1] =  rst[-1] + fill * (((len(s) - 1) // k + 1) * k - len(s))

#         return rst

# S = Solution()
# s = "abcdefghi"
# k = 3
# fill = "x"

# s = "abcdefghij"
# k = 3
# fill = "x"
# print(S.divideString(s,k,fill))
