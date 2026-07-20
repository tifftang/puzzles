class Solution:
    def findOrder(self, numCourses: int, prerequisites: List[List[int]]) -> List[int]:
        adj = defaultdict(list)
        
        for course, prereq in prerequisites:
            adj[course].append(prereq)
        result = []
        visiting = set()
        visited = set()
        def dfs(course):
            print(course)
            if course in visited: return True
            if course in visiting: return False
            visiting.add(course)
            for prereq in adj[course]:
                if not dfs(prereq): return False
            result.append(course)
            visited.add(course)
            visiting.remove(course)
            return True

        for i in range(numCourses):
            if not dfs(i): return []
        return result
        