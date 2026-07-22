class Solution:
    def solve(self, board: List[List[str]]) -> None:
        rows, cols = len(board), len(board[0])
        visited = set()

        def dfs(r, c):
            dir = [(0, 1),(0,-1),(1,0),(-1,0)]
            for d1, d2 in dir:
                x, y = d1 + r, d2 + c
                if x >= 0 and y >= 0 and x < rows and y < cols and board[x][y] == "O" and (x, y) not in visited:
                    visited.add((x, y))
                    dfs(x, y)
        for c in range(cols):
            if board[0][c] == "O":
                visited.add((0, c))
                dfs(0, c)
            if board[rows-1][c] == "O":
                visited.add((rows-1,c))
                dfs(rows-1, c)
        for r in range(rows):
            if board[r][0] == "O":
                visited.add((r, 0))
                dfs(r, 0)
            if board[r][cols-1] == "O":
                visited.add((r, cols-1))
                dfs(r, cols-1)
        for r in range(1, rows-1):
            for c in range(1, cols-1):
                if board[r][c] == "O" and (r, c) not in visited:
                    board[r][c] = "X"