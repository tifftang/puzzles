class Solution:
    def accountsMerge(self, accounts: List[List[str]]) -> List[List[str]]:
        visited = set()
        adj = defaultdict(list)
        ans = []
        for account in accounts:
            for i in range(1, len(account) - 1):
                a1 = account[i]
                a2 = account[i + 1]
                adj[a1].append(a2)
                adj[a2].append(a1)
        def dfs(acc, parent, res):
            if acc in visited: return
            res.append(acc)
            visited.add(acc)
            for next_acc in adj[acc]:
                if next_acc != parent:
                    dfs(next_acc, acc, res)
            return res
        for account in accounts:
            name = account[0]
            email = account[1]
            result = dfs(email, "", [])
            if result:
                ans.append([name] + result)
        return ans