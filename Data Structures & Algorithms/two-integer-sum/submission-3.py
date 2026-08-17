class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        hash = {}

        for i, x in enumerate(nums):
            need = target - x
            if need in hash:
                return [hash[need], i]
            hash[x] = i