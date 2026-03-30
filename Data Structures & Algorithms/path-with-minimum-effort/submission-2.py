class Solution:
    def minimumEffortPath(self, heights: List[List[int]]) -> int:
        if not heights or not heights[0]:
            return 0

        m, n = len(heights), len(heights[0])
        directions = ((0, 1), (1, 0), (0, -1), (-1, 0))

        # Tighter upper bound: max - min in the grid (<= 1e6 per constraints)
        mx = max(max(row) for row in heights)
        mn = min(min(row) for row in heights)
        left, right = 0, mx - mn
        ans = right

        def can_reach(limit: int) -> bool:
            # Iterative DFS to avoid recursion depth issues
            visited = [[False] * n for _ in range(m)]
            stack = [(0, 0)]
            visited[0][0] = True

            while stack:
                r, c = stack.pop()
                if r == m - 1 and c == n - 1:
                    return True

                cur_h = heights[r][c]
                for dr, dc in directions:
                    nr, nc = r + dr, c + dc
                    if 0 <= nr < m and 0 <= nc < n and not visited[nr][nc]:
                        if abs(heights[nr][nc] - cur_h) <= limit:
                            visited[nr][nc] = True
                            stack.append((nr, nc))

            return False

        while left <= right:
            mid = (left + right) // 2
            if can_reach(mid):
                ans = mid
                right = mid - 1
            else:
                left = mid + 1

        return ans      