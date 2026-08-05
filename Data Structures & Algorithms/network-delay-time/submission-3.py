class Solution:
    def networkDelayTime(self, times: List[List[int]], n: int, k: int) -> int:
        adj = defaultdict(list)
        for u, v, t in times:
            adj[u].append((t, v))
        
        q = [(0,k)]
        cost = [float('inf')] * (n + 1)
        cost[k] = 0
        while q:
            t, v = heapq.heappop(q)
            if cost[v] < t:
                continue
            for next_t, next_v in adj[v]:
                next_cost = next_t + t
                if cost[next_v] > next_cost:
                    cost[next_v] = next_cost
                    q.append((next_cost, next_v))
        val = max(cost[1:])
        return val if val != float('inf') else -1
