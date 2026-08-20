class Solution:
    def decodeString(self, s: str) -> str:
        stack = []
        curr = []
        num = 0
        for ch in s:
            if ch.isnumeric():
                num = num * 10 + int(ch)
            elif ch == "[":
                stack.append((num, curr))
                num = 0
                curr = []
            elif ch == "]":
                m, prev = stack.pop()
                print(m, prev, curr)
                curr = ["".join(prev) + "".join(curr) * m]
            else:
                curr.append(ch)
        return "".join(curr)