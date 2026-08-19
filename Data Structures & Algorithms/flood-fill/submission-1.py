class Solution:
    def floodFill(self, image: List[List[int]], sr: int, sc: int, color: int) -> List[List[int]]:
        
        starting_color = image[sr][sc]

        q = [(sr, sc)]
        d = [(0, 1), (0, -1), (1, 0), (-1, 0)]
        visit = set()
        while q:
            x, y = q.pop()
            image[x][y] = color
            for i, j in d:
                new_x, new_y = x + i, y + j
                if new_x >= 0 and new_y >= 0 and new_x < len(image) and new_y < len(image[0]) and image[new_x][new_y] == starting_color and (new_x, new_y) not in visit:
                    q.append((new_x, new_y))
                    visit.add((new_x, new_y))
        return image
            
