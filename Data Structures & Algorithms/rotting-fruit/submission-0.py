class Solution:
    def orangesRotting(self, grid: List[List[int]]) -> int:
        m = len(grid)
        n = len(grid[0])
        q = deque()
        time, fresh = 0, 0

        for r in range(m):
            for c in range(n):
                if grid[r][c] == 1:
                    fresh += 1
                if grid[r][c] == 2:
                    q.append([r, c])
         
                
        directions = [(1, 0), (0, 1), (-1, 0), (0, -1)]

        while q and fresh > 0:

            for i in range(len(q)):
                r, c = q.popleft()
                for dr, dc in directions:
                    nr, nc = dr + r, dc + c
                    # if in bounds and fresh, make rotten

                    if (0 > nr or nr == m or
                        0 > nc or nc == n or 
                        grid[nr][nc] != 1):
                        continue
                    grid[nr][nc] = 2
                    q.append([nr, nc])
                    fresh -= 1
            time += 1
        
        return time if fresh == 0 else -1