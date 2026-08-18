class Solution:
    def findMinHeightTrees(self, n: int, edges: List[List[int]]) -> List[int]:
        adj = defaultdict(list)
        for a, b in edges:
            adj[a].append(b)
            adj[b].append(a)
        
        minH = float('inf')
        d = defaultdict(list)

        for i in range(n):
            q = deque([i])
            visited = {i}
            levels = 0
            while q:
                for _ in range(len(q)):
                    node = q.popleft()
                    for next_node in adj[node]:
                        if next_node not in visited:
                            visited.add(next_node)
                            q.append(next_node)
                levels += 1
            if levels <= minH:
                minH = levels
                d[minH].append(i)
        return d[minH]