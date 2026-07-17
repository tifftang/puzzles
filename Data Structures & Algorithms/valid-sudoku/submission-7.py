class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        seen = set()

        for r in range(len(board)):
            seen = set()
            for c in range(len(board[0])):
                if board[r][c] != '.' and board[r][c] in seen:
                    return False
                seen.add(board[r][c])
        for c in range(len(board[0])):
            seen = set()
            for r in range(len(board)):
                if board[r][c] != '.' and board[r][c] in seen:
                    return False
                seen.add(board[r][c])        
        for i in range(0, 9, 3):
            
            for j in range(0, 9, 3):
                seen = set()
                for c in range(j, j + 3):
                    for r in range(i, i + 3):
                        if board[r][c] != '.' and board[r][c] in seen:
                            return False
                        seen.add(board[r][c])  

                
        return True