class Solution:
    def maxAreaOfIsland(self, grid: List[List[int]]) -> int:
        rows, cols = len(grid), len(grid[0])
        area = 0
        visit = set()

        def dfs(r, c):
            if r >= rows or c >= cols or r < 0 or c < 0 or grid[r][c] == 0:
                return 0
            if (r, c) in visit:
                return 0
            visit.add((r, c))
            area = 1

            area += dfs(r+1, c)
            area += dfs(r-1, c)
            area += dfs(r, c+1)
            area += dfs(r, c-1)
            return area

        for r in range(rows):
            for c in range(cols):
                if grid[r][c] == 1 and (r, c) not in visit:
                    area = max(area, dfs(r ,c))
        
        return area