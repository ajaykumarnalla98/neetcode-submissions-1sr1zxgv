class Solution:
    def firstMissingPositive(self, nums: List[int]) -> int:
        n = len(nums)
        
        for i in range(n):
            if nums[i] < 0 or nums[i] > n:
                nums[i] = 0

        for i in range(n):
            while 1 <= nums[i] <= n:
                correct_index = nums[i]-1
                if nums[correct_index] == nums[i]:
                    break
                nums[i], nums[correct_index] = nums[correct_index], nums[i]
        
        for i in range(n):
            if nums[i] != i+1:
                return i+1
        return n+1