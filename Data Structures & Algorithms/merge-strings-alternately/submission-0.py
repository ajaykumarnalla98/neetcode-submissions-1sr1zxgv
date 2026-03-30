class Solution:
    def mergeAlternately(self, word1: str, word2: str) -> str:
        i, j = 0, 0
        res = []
        a = len(word1)
        b = len(word2)

        while i < a or j < b:
            if i < a:
                res.append(word1[i])
                i += 1
            if j < b:
                res.append(word2[j])
                j += 1
        return "".join(res)       