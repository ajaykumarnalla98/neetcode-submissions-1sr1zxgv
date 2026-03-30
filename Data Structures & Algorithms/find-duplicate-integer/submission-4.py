class Solution:
    def findDuplicate(self, nums: List[int]) -> int:
        nums.sort()
        i, j = 0, len(nums) - 1
        for i in range(j):
            if nums[i] == nums[i+1]:
                return nums[i]
        return -1
