class Solution:
    def solve(self, board: List[List[str]]) -> None:
        m = len(board)
        n = len(board[0])
        directions = [(1, 0), (0, 1), (-1, 0), (0, -1)]
        
        def capture(): 
            q = deque()
            for r in range(m):
                for c in range(n):
                    if (r == 0 or r == m - 1 or 
                        c == 0 or c == n - 1 and 
                        board[r][c] == "O"
                    ):
                        q.append((r, c))
            
            while q:
                r, c = q.popleft()
                if board[r][c] == "O":
                    board[r][c] = "T"
                    for dr, dc in directions:
                        nr, nc = r + dr, c + dc
                        if 0 <= nr < m and 0 <= nc< n:
                            q.append((nr, nc))
        
        capture()
        for r in range(m):
            for c in range(n):
                if board[r][c] == "O":
                    board[r][c] = "X"
                elif board[r][c] == "T":
                    board[r][c] = "O"