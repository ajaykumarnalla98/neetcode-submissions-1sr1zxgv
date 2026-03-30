class Solution:
    def combine(self, n: int, k: int) -> List[List[int]]:
        res = []

        def dfs(i, combo):
            if len(combo) == k:
                res.append(combo[:])
                return 

            for num in range(i, n+1):
                combo.append(num)
                dfs(num+1, combo)
                combo.pop()

        dfs(1, [])
        return res