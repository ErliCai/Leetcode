class Solution(object):
    def productExceptSelf(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """

        products = [1]
        products_reverse = [1]
        n1 = n2 = 1
        for i in nums:
            products.append(n1)
            n1 = n1 * i
        for i in nums[::-1]:
            products_reverse.append(n2)
            n2 = n2 * i

        products_reverse = products_reverse[::-1]

        return [products_reverse[i] * products[i] for i in range(len(nums))]