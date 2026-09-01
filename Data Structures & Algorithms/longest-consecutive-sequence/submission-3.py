class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        num_set = set(nums)
        count = 0
        for n in nums:
            if (n-1) not in num_set:
                length = 1
                while (n+length) in num_set:
                    length += 1
                count = max(count, length) 
        return count