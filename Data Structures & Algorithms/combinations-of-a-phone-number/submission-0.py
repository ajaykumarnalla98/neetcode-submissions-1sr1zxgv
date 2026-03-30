class Solution:
    def letterCombinations(self, digits: str) -> List[str]:
        if not digits: 
            return []
        
        res = []
        mapping = {"2":"abc", "3":"def", "4":"ghi", "5":"jkl", "6":"mno", "7":"pqrs", "8":"tuv", "9":"wxyz"}
        def dfs(index, path):
            if len(path) == len(digits):
                res.append("".join(path))
                return
            
            for char in mapping[digits[index]]:
                path.append(char)
                dfs(index + 1, path)
                path.pop()

        dfs(0, [])
        return res
