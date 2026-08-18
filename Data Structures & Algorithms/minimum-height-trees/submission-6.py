class Solution:
    def findMinHeightTrees(self, n: int, edges: List[List[int]]) -> List[int]:
        adj = defaultdict(set)
        if not edges: return [0]
        for a, b in edges:
            adj[a].add(b)
            adj[b].add(a)
        q = deque()
        result = set([i for i in range(n)])
        for i in range(n):
            if len(adj[i]) == 1:
                q.append(i)
        while len(result) > 2:
            for _ in range(len(q)):
                i = q.popleft()
                for n in adj[i]:
                    adj[n].remove(i)
                    result.remove(i)
                    if len(adj[n]) == 1:
                        q.append(n)
                        
                del adj[i]
        return list(result)