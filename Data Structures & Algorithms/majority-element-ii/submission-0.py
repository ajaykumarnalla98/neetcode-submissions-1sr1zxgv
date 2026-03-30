class Solution:
    def majorityElement(self, nums: List[int]) -> List[int]:
        n = len(nums)
        k = n // 3 
        freq = {} 

        for x in nums:
            freq[x] = freq.get(x , 0) + 1

        result = []
        for key, cnt in freq.items():
            if cnt > k:
                result.append(key)

        return result  