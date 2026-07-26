class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        rows, cols = len(matrix), len(matrix[0])
        row = -1

        l, r = 0, rows - 1
        while l <= r:
            mid = l + (r - l)//2
            if target >= matrix[mid][0] and target <= matrix[mid][cols - 1]:
                row = mid
                break
            elif target > matrix[mid][cols - 1]:
                l = mid + 1
            else:
                r = mid - 1
        if row < 0: return False

        l, r = 0, cols - 1

        while l <= r:
            mid = l + (r - l)//2
            if matrix[row][mid] == target: return True
            elif matrix[row][mid] < target:
                l = mid + 1
            else:
                r = mid - 1
        return False