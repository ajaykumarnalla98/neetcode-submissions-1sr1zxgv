class Solution:
    def containsNearbyDuplicate(self, nums: List[int], k: int) -> bool:
        hashset = {}

        for i, n in enumerate(nums):
            if n in hashset and i - hashset[n] <= k:
                    return True
            hashset[n] = i
        return False       