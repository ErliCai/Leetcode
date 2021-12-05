class Solution(object):
    def calculate(self, s):
        """
        :type s: str
        :rtype: int
        """

        s = "".join([char for char in s if char != " "])
        
        last = 0
        signs = {"+", "-", "*", "/"}
        l = []
        for i in range(len(s)):
            if s[i] in signs:
                l.append(s[last:i])
                l.append(s[i])
                last = i+1

        l.append(s[last:])
        print(l)
        l = [int(i) if i.isnumeric() else i for i in l]
        
        print(l)

        def compute(i, j , sign):
            if sign == "+":
                return i + j
            elif sign == "-":
                return i - j
            elif sign == "*":
                return i * j
            elif sign == "/":
                print(i, j)
                return i / j

        def compute_for_signs(l, signs):
            new_l = []
            last = None
            last_sign = None
            last_is_sign = False
            for i in l:
                if i in signs:
                    last_is_sign = True
                    last_sign = i
                else:
                    if not last_is_sign:
                        if last is not None:
                            new_l.append(last)
                        last = i
                    else:
                        last = compute(last, i, last_sign)
                        last_is_sign = False
            new_l.append(last)
            return new_l


        # compute multiplication and division first
        l = compute_for_signs(l, {"*", "/"})
        l = compute_for_signs(l, {"+", "-"})

        return l[0]
                
    


S = Solution()
s = "32+2*2"
S.calculate(s)