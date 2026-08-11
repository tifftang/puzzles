class Solution:
    def checkIfPrerequisite(self, numCourses: int, prerequisites: List[List[int]], queries: List[List[int]]) -> List[bool]:
        adj = defaultdict(list)
        for pre, course in prerequisites:
            adj[course].append(pre)
        
        d = defaultdict(set)

        def dfs(course):
            visit = set()
            if course in d: 
                visit.update(d[course])
                visit.add(course)
                return visit
            for pre in adj[course]:
                visit.update(dfs(pre))
            d[course] = set(visit)
            visit.add(course)
            return visit
        ans = [False] * len(queries)

        for idx, (u, v) in enumerate(queries):
            dfs(v)
            print(d[v], v)
            if u in d[v]: 
                ans[idx] = True
        print(d, adj)
        return ans