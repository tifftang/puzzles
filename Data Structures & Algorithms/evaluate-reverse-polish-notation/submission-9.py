class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        stack = []
        for t in tokens:
            #print(stack)
            if t.isnumeric() or (t[0] == "-" and len(t) > 1):
                stack.append(int(t))
            else:
                b = stack.pop()
                a = stack.pop()
                if t == "+":
                    stack.append(a + b)
                elif t == "*":
                    stack.append(a * b)
                elif t == "-":
                    stack.append(a - b)
                else:
                    stack.append(int(a / b))
        return stack[-1]
