"""
# Definition for a QuadTree node.
class Node:
    def __init__(self, val, isLeaf, topLeft, topRight, bottomLeft, bottomRight):
        self.val = val
        self.isLeaf = isLeaf
        self.topLeft = topLeft
        self.topRight = topRight
        self.bottomLeft = bottomLeft
        self.bottomRight = bottomRight
"""

class Solution:
    def construct(self, grid: List[List[int]]) -> 'Node':
        def dfs(r, c, size):
            first = grid[r][c]
            uniform = True

            for i in range(r, r+size):
                for j in range(c, c+size):
                    if grid[i][j] != first:
                        uniform = False
                        break
                if not uniform:
                    break
                
            if uniform:
                return Node(first, True, None, None, None, None)

            half = size // 2
            return Node(
                True,
                False,
                dfs(r, c, half),
                dfs(r, c+half, half),
                dfs(r+half, c, half),
                dfs(r+half, c+half, half)
            )
        return dfs(0, 0, len(grid))
        