class Solution:
    def countComponents(self, n: int, edges: List[List[int]]) -> int:
        adj = defaultdict(list)
        for a, b in edges:
            adj[a].append(b)
            adj[b].append(a)
        
        visited = set()

        def dfs(node):
            for next_node in adj[node]:
                if next_node not in visited:
                    visited.add(next_node)
                    dfs(next_node)
            
            return
        num_c = 0

        for i in range(n):
            if i not in visited:
                dfs(i)
                num_c += 1
        return num_c