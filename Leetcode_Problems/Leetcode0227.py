class Solution(object):
    def calculate(self, s):
        """
        :type s: str
        :rtype: int
        """
        

        s_wo0 = [i for i in s if i != " "]
        s_int = []
        acc = 0
        operators = set(["+","-","*","/"])
        for n in range(len(s_wo0)):
            s = s_wo0[n]
            if s in operators:
                s_int.append(acc)
                s_int.append(s)
                acc = 0
            else:
                acc *= 10
                acc += int(s)
        s_int.append(acc)

        print("s_int", s_int)
        stack = ["null",]
        for n in s_int:
            
            if stack[-1] == "*" or stack[-1] == "/" :
                operator = stack.pop()
                n1 = stack.pop()
                if operator == "*":
                    stack.append(n * n1)
                if operator == "/":
                    stack.append(n1 // n)                    
            else:
                stack.append(n)

        stack.pop(0)

        ans = stack[0]
        symbol = None
        for n in range(1, len(stack)):
            if stack[n] == "+":
                symbol = "+"
            elif stack[n] == "-":
                symbol = "-"
            else:
                if symbol == "+":
                    ans += stack[n]
                else:
                    ans -= stack[n]
        return ans

S = Solution()
s = "3/2"
print(S.calculate(s))