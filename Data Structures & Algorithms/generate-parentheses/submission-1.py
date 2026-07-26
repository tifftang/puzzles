class Solution:
    def generateParenthesis(self, n: int) -> List[str]:
        result = []
        def bt(open, close, ans):
            if not open and not close:
                result.append("".join(ans))
                return
            
            if open:
                bt(open - 1, close, ans + ["("])
            if open < close:
                bt(open, close - 1, ans + [")"])
        bt(n, n, [])
        return result