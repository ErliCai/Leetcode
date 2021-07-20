import operator

class Solution:
    def evalRPN(self, tokens):
        
        ops = {"+" : operator.add, "-" : operator.sub,
            "/" : operator.truediv, "*" : operator.mul}

        operators = "+-*/"
        stack = []
        while tokens:
            a = tokens.pop()
            if a in operators:
                stack.append(a)
            else:
                if len(stack) >= 2 and stack[-2] in operators:
                    b = stack.pop()
                    o = stack.pop()
                    c = str(ops[o](int(b), int(a)))
                    tokens.append(c)
                else:
                    stack.append(a)
            #print(tokens, stack)
            
        return stack[0]

S = Solution()
tokens = ["2","1","+","3","*"]
print(S.evalRPN(tokens))