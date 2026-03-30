class Solution:
    def combinationSum(self, nums: List[int], target: int) -> List[List[int]]:
        res = []
        
        def dfs(i, combo, sum):
            if sum == target:
                res.append(combo[:])
                return
            
            if sum > target:
                return
            
            for j in range(i, len(nums)):
                combo.append(nums[j])
                dfs(j, combo, sum+nums[j])
                combo.pop()
        
        dfs(0, [], 0)
        return res