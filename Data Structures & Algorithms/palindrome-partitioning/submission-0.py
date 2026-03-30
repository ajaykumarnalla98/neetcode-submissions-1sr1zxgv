class Solution:
    def partition(self, s: str) -> List[List[str]]:
        res = []

        def dfs(start, path):
            if start == len(s):
                res.append(path[:])
                return 

            for end in range(start + 1, len(s) + 1):
                sub = s[start:end]
                if sub == sub[::-1]:
                    path.append(sub)
                    dfs(end, path)
                    path.pop()

        dfs(0, [])
        return res   