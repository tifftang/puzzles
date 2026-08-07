class Solution:
    def minCostConnectPoints(self, points: List[List[int]]) -> int:
        if len(points) == 1: return 0
        d = defaultdict(list)
        for i in range(len(points)):
            for j in range(i + 1, len(points)):
                x, y = points[i]
                a, b = points[j]
                dist = abs(x - a) + abs(y - b)
                d[i].append((dist, j))
                d[j].append((dist, i))
        # for k in d.keys():
        #     d[k] = sorted(d[k])
        
        total = 0
        done = set()
        heap = [(0, 0)]
        while heap:
            cost, idx = heapq.heappop(heap)
            if idx in done:
                continue
            x, y = points[idx]
            total += cost
            done.add(idx)
            for c, i in d[idx]:
                heapq.heappush(heap, (c, i))

        return total
