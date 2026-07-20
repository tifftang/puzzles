class Solution:
    def maxAreaOfIsland(self, grid: List[List[int]]) -> int:
        maxArea = 0
        seen = set()
        rows, cols = len(grid), len(grid[0])

        def dfs(r, c):
            dir = [(0, 1), (0, -1), (1, 0), (-1, 0)]
            seen.add((r, c))
            area = 1
            for d1, d2 in dir:
                x, y = r + d1, c + d2
                if x >= 0 and y >= 0 and x < rows and y < cols and grid[x][y] == 1 and (x, y) not in seen:
                    area += dfs(x, y)
            return area

        for r in range(rows):
            for c in range(cols):
                if grid[r][c] == 1 and (r, c) not in seen:
                    maxArea = max(maxArea, dfs(r, c))
        return maxArea