class Solution:
    def calcEquation(self, equations: List[List[str]], values: List[float], queries: List[List[str]]) -> List[float]:
        adj = defaultdict(list)

        for i, (a, b) in enumerate(equations):
            adj[a].append((b, values[i]))
            adj[b].append((a, 1/values[i]))
        
        def bfs(a, b):
            if not len(adj[a]) or not len(adj[b]):
                return -1
            if a == b:
                return 1.0
            q = deque([(a, 1)])
            visited = set([a])
            while q:
                n, v = q.popleft()
                for next_a, next_v in adj[n]:
                    if next_a not in visited:
                        visited.add(next_a)
                        if next_a == b:
                            return v * next_v
                        q.append((next_a, v * next_v))
            return -1
        return [bfs(q[0], q[1]) for q in queries]