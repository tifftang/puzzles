class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        result = [0] * len(temperatures)
        stack = []
        for idx, t in enumerate(temperatures):
            while stack and temperatures[stack[-1]] < t:
                i = stack.pop()
                result[i] = idx - i
            stack.append(idx)
        return result

