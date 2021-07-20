class Solution(object):
    def totalFruit(self, tree):
        """
        :type tree: List[int]
        :rtype: int
        """
        
        
        types = [None, None]
        begin = end = 0
        basket = [0,0]
        total = 0

        while end < len(tree):
            if tree[end] != types[1] and types[0] is None:
                types[0] = tree[end]
                basket[0] += 1
            elif tree[end] != types[0] and types[1] is None:
                types[1] = tree[end]
                basket[1] += 1
            else:

                if types[0] == tree[end]:
                    basket[0] += 1
                elif types[1] == tree[end]:
                    basket[1] += 1
                else:
                    if sum(basket) > total:
                        total = sum(basket)
                    while 0 not in basket:
                        i = types.index(tree[begin])
                        basket[i] -= 1
                        begin += 1
                    types[basket.index(0)] = None
                    end -= 1    
            end += 1
        if sum(basket) > total:
            total = sum(basket)
        return total


S = Solution()
input = [1,2,3,2,2]
print(S.totalFruit(input))