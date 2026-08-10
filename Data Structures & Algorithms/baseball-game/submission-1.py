class Solution:
    def calPoints(self, operations: List[str]) -> int:
        stack = []

        for op in operations:
            if op.isnumeric() or op[0] == '-':
                stack.append(int(op))
            elif op == "+":
                a = stack[-1]
                b = stack[-2]
                stack.append((a + b))
            elif op == "D":
                stack.append(2*stack[-1])
            else:
                stack.pop()
        #print(stack)
        return sum(stack)