class Solution:
    def containsNearbyDuplicate(self, nums: List[int], k: int) -> bool:
        last = {}

        for i, j in enumerate(nums):
            if j in last and i - last[j] <= k:
                    return True
            last[j] = i
        return False       