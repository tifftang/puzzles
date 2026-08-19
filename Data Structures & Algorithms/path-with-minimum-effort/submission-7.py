class Solution:
    def minimumEffortPath(self, heights: List[List[int]]) -> int:
        q = [(0, (0, 0))]
        d = [(0, 1), (0, -1), (1, 0), (-1, 0)]
        visited = defaultdict(int)
        visited[(0,0)] = 0
        rows, cols = len(heights) - 1, len(heights[0]) - 1
        if 0 == (len(heights) - 1) and 0 == (len(heights[0]) - 1): return 0
        while q:
            cost, (x, y) = heapq.heappop(q)
            
            for i, j in d:
                new_x, new_y = x + i, y + j
                if new_x >= 0 and new_y >= 0 and new_x < len(heights) and new_y < len(heights[0]):
                    new_cost = max(cost, abs(heights[x][y] - heights[new_x][new_y]))
                    if (new_x, new_y) not in visited or visited[(new_x, new_y)] > new_cost:
                        visited[(new_x, new_y)] = new_cost
                        heapq.heappush(q, (new_cost, (new_x, new_y)))
        return visited[(rows, cols)]

