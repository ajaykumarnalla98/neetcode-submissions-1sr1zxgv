class Solution:
    def combinationSum2(self, candidates: List[int], target: int) -> List[List[int]]:
        candidates = sorted(candidates)
        res = []

        def dfs(i, currCombo, total):
            if total == target:
                res.append(currCombo[:])
                return
            if total > target:
                return 
            
            for j in range(i, len(candidates)):
                if j > i and candidates[j] == candidates[j-1]:
                    continue
                
                num = candidates[j]
                currCombo.append(num)
                dfs(j+1, currCombo, total+num)
                currCombo.pop()

        dfs(0, [], 0)
        return res
