class Solution:
    def findItinerary(self, tickets: List[List[str]]) -> List[str]:
        tickets.sort(reverse=True)
        #print(tickets)
        adj = defaultdict(list)
        for origin, dest in tickets:
            adj[origin].append(dest)
        #print(adj)
        result = []
        def dfs(airport):
            while adj[airport]:
                dfs(adj[airport].pop())
            adj[airport] = []
            result.append(airport)
        dfs("JFK")
        result.reverse()
        return result