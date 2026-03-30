class Solution:
    def findDuplicate(self, nums: List[int]) -> int:
        hash = set()
        for n in nums:
            if n in hash:
                return n
            hash.add(n)
        return -1     