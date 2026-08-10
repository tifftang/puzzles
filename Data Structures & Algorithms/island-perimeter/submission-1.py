class Solution:
    def islandPerimeter(self, grid: List[List[int]]) -> int:
        
        def checkNeighbors(x, y):
            if grid[x][y] == 0: return 4
            d = [(0, 1), (1, 0), (0, -1), (-1, 0)]
            neis = 0
            for r, c in d:
                n_x, n_y = r + x, c + y
                if n_x >= 0 and n_y >= 0 and n_x < len(grid) and n_y < len(grid[0]) and grid[n_x][n_y] == 1:
                    neis += 1
            return neis
        result = 0
        for i in range(len(grid)):
            for j in range(len(grid[0])):
                neis = checkNeighbors(i, j)
                result += (4 - neis)
        return result