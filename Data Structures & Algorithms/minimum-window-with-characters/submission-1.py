class Solution:
    def minWindow(self, s: str, t: str) -> str:
        if not t: return ""
        need, window = Counter(t), {}
        have = 0
        res, res_len = "", float("inf")
        l = 0

        for r, c in enumerate(s):
            window[c] = window.get(c, 0) + 1
            if c in need and window[c] == need[c]:
                have += 1

            while have == len(need):
                if (r - l + 1) < res_len:
                    res, res_len = s[l:r+1], (r - l + 1)
                window[s[l]] -= 1
                if s[l] in need and window[s[l]] < need[s[l]]:
                    have -= 1
                l += 1

        return res