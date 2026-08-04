class Solution:
    def largestRectangleArea(self, heights: List[int]) -> int:
        stack = []
        area = 0
        heights = heights + [0]
        for i in range(len(heights)):
            while stack and heights[stack[-1]] > heights[i]:
                idx = stack.pop()
                if stack:
                    l = stack[-1] 
                    area = max(area, heights[idx] * (i - l - 1))
                else:
                    area = max(area, heights[idx] * (i))
            stack.append(i)
        return area

