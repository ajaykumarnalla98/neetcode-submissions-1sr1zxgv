class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        if len(s) != len(t):
            return False
        count_map = {}

        for c in s:
            count_map[c] = count_map.get(c, 0) + 1

        for c in t:
            if c not in count_map:
                return False
            count_map[c] -= 1
            if count_map[c] < 0:
                return False   
        return True