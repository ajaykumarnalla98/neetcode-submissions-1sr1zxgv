class Solution:
    def canPartitionKSubsets(self, nums: List[int], k: int) -> bool:
        total = sum(nums)
        if total % k != 0:
            return False

        target = total // k
        nums.sort(reverse=True)

        buckets = [0] * k
        
        def backtrack(index):
            if index == len(nums):
                return True

            for i in range(k):
                if buckets[i] + nums[index] > target:
                    continue

                if i > 0 and buckets[i] == buckets[i-1]:
                    continue

                buckets[i] += nums[index]
                if backtrack(index+1):
                    return True
                buckets[i] -= nums[index]
            return False

        return backtrack(0)        