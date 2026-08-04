class Solution:
    def networkDelayTime(self, times: List[List[int]], n: int, k: int) -> int:
        adj = defaultdict(list)
        cost = defaultdict(int)
        costs = [float('inf')] * (n + 1)
        for u, v, c in times:
            adj[u].append(v)
            cost[(u, v)] = c
        
        q = [(0, k)]
        heapq.heapify(q)
        costs[k] = 0
        while q:
            c, node = heapq.heappop(q)
            if costs[node] < c:
                continue
            for next_node in adj[node]:
                new_cost = c + cost[(node, next_node)]
                if costs[next_node] > new_cost:
                    costs[next_node] = new_cost
                    heapq.heappush(q, (new_cost, next_node))
        result = 0
        costs[0] = 0
        for c in costs[1:]:
            if c == float('inf'): return -1

        return max(costs)
