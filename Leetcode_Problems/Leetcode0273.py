from curses.ascii import SO


class Solution(object):
    def numberToWords(self, num):
        """
        :type num: int
        :rtype: str
        """

        if num == 0:
            return "Zero"

        first_digit = {1:"One", 2:"Two", 3: "Three", 4:"Four", 5:"Five", 6:"Six", 7:"Seven", 8:"Eight", 9:"Nine", 10:"Ten",
        11:"Eleven", 12:"Twelve", 13:"Thirteen", 14:"Fourteen", 15:"Fifteen", 16:"Sixteen", 17:"Seventeen", 18:"Eighteen", 19:"Nineteen"}
        second_digit = {2:"Twenty", 3:"Thirty", 4:"Forty", 5:"Fifty", 6:"Sixty", 7:"Svenety", 8:"Eighty", 9:"Ninety"}

        order = 0

        rst = []

        while num > 0:
            num, n = num // 1000, num % 1000

            if n == 0:
                order += 1
                continue

            s = []
            if (n % 100) < 20:
                s.append(first_digit[n % 100])
            else:
                s.append(second_digit[(n//10)%10])
                s.append(first_digit[n%10])

            if n >= 100:
                s = [first_digit[n//100] , "Hundred"] + s
            if order == 1:
                s.append("Thousand")
            if order == 2:
                s.append("Million")
            if order == 3:
                s.append("Billion")
            rst = s + rst
            order += 1

        return rst


S = Solution()
num = 123
print(S.numberToWords(num))

num = 10001
print(S.numberToWords(num))