from os import error


class Solution(object):
    def evalRPN(self, tokens):
        """
        :type tokens: List[str]
        :rtype: int
        """
        
        def cal(a,b,o):
            if o == "+":
                return a + b
            if o == "-":
                return a - b
            if o == "*":
                return a * b
            if o == "/":
                return a / b

        stack = ["dummy"]
        operators = set(["+","-","*","/"])
        for t in tokens[::-1]:
            if t in operators:
                stack.append(t)
            else:
                stack.append(int(t))
                while stack[-2] not in operators:
                    a = stack.pop()
                    b = stack.pop()
                    o = stack.pop()
                    stack.append(cal(a, b, o))

        return stack[1]

print( 6 // 132)