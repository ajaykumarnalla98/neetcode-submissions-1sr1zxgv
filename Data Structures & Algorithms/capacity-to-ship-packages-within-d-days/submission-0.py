class Solution:
    def shipWithinDays(self, weights: List[int], days: int) -> int:
        def canShip(cap):
            d = 1
            cur = 0
            for w in weights:
                if cur + w > cap:
                    d += 1
                    cur = 0
                cur += w
            return d <= days

        l, r = max(weights), sum(weights)
        
        while l < r:
            m = (l + r) // 2
            if canShip(m):
                r = m
            else:
                l = m + 1
        return l