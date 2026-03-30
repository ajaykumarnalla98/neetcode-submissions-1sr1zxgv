class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:

        graph = {i: [] for i in range(numCourses)}
        for a, b in prerequisites:
            graph[a].append(b)

        visiting, visited = set(), set()

        def dfs(a):
            if a in visiting:
                return False
            if a in visited:
                return True
            
            visiting.add(a)
            for b in graph[a]:
                if not dfs(b):
                    return False
            visiting.remove(a)
            visited.add(a)
            return True

        for a in range(numCourses):
            if not dfs(a):
                return False
        return True