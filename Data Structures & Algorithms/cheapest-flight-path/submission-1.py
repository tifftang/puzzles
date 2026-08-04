class Solution:
    def findCheapestPrice(self, n: int, flights: List[List[int]], src: int, dst: int, k: int) -> int:
        adj = defaultdict(list)
        costs = defaultdict(int)
        result = {i: float('inf') for i in range(n)}

        for s, d, c in flights:
            adj[s].append(d)
            costs[(s, d)] = c
        q = deque([(src, 0)])
        stops = 0
        while q:
            #print(q)
            for _ in range(len(q)):
                node, cost = q.popleft()
                if result[node] > cost:
                    result[node] = cost
                    if stops < k + 1:
                        for next_dst in adj[node]:
                            next_cost = cost + costs[(node, next_dst)]
                            q.append((next_dst, next_cost))
            stops += 1
        return -1 if result[dst] == float('inf') else result[dst]


