class Solution(object):
    def coinChange(self, coins, amount):
        """
        :type coins: List[int]
        :type amount: int
        :rtype: int
        """
        
        coin_set = set(coins)
        amount_set = {c for c in coins if c < amount}

        i = 1
        while amount_set:
            if amount in amount_set:
                return i
            else:
                amount_temp = set()
                for a in amount_set:
                    for c in coin_set:
                        if a + c <= amount:
                            amount_temp.add(a+c)    
                amount_set = amount_temp        
            i += 1

        return -1