class Solution:
    def findMedianSortedArrays(self, nums1: List[int], nums2: List[int]) -> float:
        A, B = nums1, nums2
        if len(A) > len(B):
            A, B = B, A

        m, n = len(A), len(B)
        total = m + n
        half = total // 2

        l, r = 0, m
        while l <= r:
            x = (l + r) // 2
            y = half - x

            maxLeftA = A[x-1] if x > 0 else float('-inf')
            minRightA = A[x] if x < m else float('inf')

            maxLeftB = B[y-1] if y > 0 else float('-inf')
            minRightB = B[y] if y < n else float('inf')

            if maxLeftA <= minRightB and maxLeftB <= minRightA:
                if total % 2:
                    return min(minRightA, minRightB)
                return (max(maxLeftA, maxLeftB) + min(minRightA, minRightB)) / 2 
            elif maxLeftA > minRightB:
                r = x - 1
            else:
                l = x + 1      