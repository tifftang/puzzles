class Solution:
    def findClosestElements(self, arr: List[int], k: int, x: int) -> List[int]:
        closest = deque([])

        for v in arr:
            closest.append(v)
            if len(closest) > k:
                l, r = 0, len(closest) - 1
                a, b = closest[l], closest[r]
                if abs(a-x) < abs(b-x) or abs(a-x) == abs(b-x):
                    closest.pop()
                else:
                    closest.popleft()
        return list(closest)