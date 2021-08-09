class Solution(object):
    def sumSubarrayMins(self, arr):
        """
        :type arr: List[int]
        :rtype: int
        """
        
        length = len(arr)
        range_mul = [None] * length

        def cal_mul(l, r, i):
            r = r - i
            l = i - l + 1
            return l * r
        for i in range(length):
            v = arr[i]
            left, right = None, None
            for j in range(i):
                if arr[i-j-1]  <= v:
                    left = i-j
                    break
            if left is None:
                left = 0

            for j in range(i+1, length):
                if arr[j]  < v:
                    right = j
                    break
            if right is None:
                right = length

            # if not flag:
            #     range_mul[i] = [left,right]
            # else:
            #     range_mul[i] = None
            range_mul[i] = [left,right]

        ans = 0
        for i in range(length):
            if range_mul[i]:
                l, r = range_mul[i]
                mul = cal_mul(l, r, i)
                ans += int(arr[i] * mul)
                ans = ans % (10**9 + 7)
                #print(arr[i], r, ans)
                print(l, r, i)

        print(arr[500], cal_mul(0, 1000, 500))

        return ans % (10**9 + 7)




class Solution2(object):
    def sumSubarrayMins(self, arr):
        """
        :type arr: List[int]
        :rtype: int
        """
    
        if not arr:
            return 0

        length = len(arr)
        
        m = min(arr)
        m_index, arr_len = arr.index(m), len(arr)

        def cal_mul(l, r, i):
            r = r - i
            l = i - l + 1
            return l * r

        ans = m * cal_mul(0, length, m_index)

        return (self.sumSubarrayMins(arr[:m_index]) + self.sumSubarrayMins(arr[m_index+1:]) + ans)  % (10**9 + 7)












class Solution3(object):
    def sumSubarrayMins(self, arr):
        """
        :type arr: List[int]
        :rtype: int
        """

        arr = [float('-inf')] + arr + [float('-inf')]
        length = len(arr)
        range_mul = [None] * length
        ans = 0

        def cal_mul(l, r, i):
            r = r - i
            l = i - l + 1
            return l * r

        stack = []
        for i in range(length):
            v = arr[i]
            while stack and arr[stack[-1]] > v:
                cur = stack.pop()
                ans += int(arr[cur] * cal_mul(stack[-1]+1, i, cur))
                
            stack.append(i)

        return ans % (10**9 + 7)

    


S = Solution3()
#arr = [3,1,2,4]
arr = [11,81,94,43,3]
#arr = [1,1,1,1,1]
print(S.sumSubarrayMins(arr))

