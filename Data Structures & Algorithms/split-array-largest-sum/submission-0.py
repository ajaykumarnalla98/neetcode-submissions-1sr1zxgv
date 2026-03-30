class Solution:
    def splitArray(self, nums: List[int], k: int) -> int:
        def canSplit(maxAllowed):
            count = 1
            currSum = 0

            for n in nums:
                if currSum + n > maxAllowed:
                    count += 1
                    currSum = n
                    if count > k:
                        return False
                else:
                    currSum += n
            return True

        l, r = max(nums), sum(nums)

        while l < r:
            m = (l + r) // 2
            if canSplit(m):
                r = m
            else:
                l = m + 1

        return l