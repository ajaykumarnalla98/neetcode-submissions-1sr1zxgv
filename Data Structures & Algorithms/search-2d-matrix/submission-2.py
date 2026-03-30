class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        m = len(matrix)
        n = len(matrix[0])
        l, r = 0, m*n-1
        while l <= r:
            x = (l+r)//2
            row = x // n
            col = x % n
            value = matrix[row][col]
            if value == target:
                return True
            elif value < target:
                l = x + 1
            else:
                r = x - 1
        return False
            