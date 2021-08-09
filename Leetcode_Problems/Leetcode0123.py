class Solution(object):
    def maxProfit(self, prices):
        """
        :type prices: List[int]
        :rtype: int
        """
        if len(prices) == 1:
            return 0

        profits = [self.max_single_transaction(prices[:i]) + self.max_single_transaction(prices[i:]) for i in range(1, len(prices) - 1)]
        p = self.max_single_transaction(prices)

        return max(profits + [p])

    def max_single_transaction(self, prices):

        min_prices_front = [0] * len(prices)
        min_price = 10 ** 5
        for i in range(len(prices)):
            if prices[i] < min_price:
                min_price = prices[i]
            min_prices_front[i] = min_price

        max_prices_back = [0] * len(prices)
        max_price = 0
        for i in range(len(prices)):

            if prices[-i - 1] > max_price:
                max_price = prices[-1 -i]
            max_prices_back[-i-1] = max_price

        profit = [max_prices_back[i] - min_prices_front[i] for i in range(len(prices))]

        return max(profit)



S = Solution()
prices = [2,1,2,0,1]
print(S.maxProfit(prices))