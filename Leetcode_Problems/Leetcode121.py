class Solution(object):
    def maxProfit(self, prices):
        """
        :type prices: List[int]
        :rtype: int
        """
        
        n = len(prices)
        list_highest = n * [0]
        list_highest[-1] = prices[-1]
        for i in range(1,n):
            list_highest[-i-1] = max(list_highest[-i], prices[-i-1])

        list_lowest = n * [0]
        list_lowest[0] = prices[0]
        for i in range(n-1):
            list_lowest[i+1] = min(list_lowest[i], prices[i+1])

        print(list_lowest)

        l = [list_highest[i] - list_lowest[i] for i in range(len(prices))]
        return max(l)


S = Solution()
prices = [7,1,5,3,6,4]
print(S.maxProfit(prices))