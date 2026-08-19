class Solution:
    def findClosestElements(self, arr: List[int], k: int, x: int) -> List[int]:
        closest = deque()

        for v in arr:
            closest.append(v)

            if len(closest) > k:
                if abs(closest[0] - x) <= abs(closest[-1] - x):
                    closest.pop()
                else:
                    closest.popleft()

        return list(closest)