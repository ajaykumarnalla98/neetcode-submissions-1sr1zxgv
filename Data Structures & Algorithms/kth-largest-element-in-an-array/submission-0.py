class Solution:
    def findKthLargest(self, nums: List[int], k: int) -> int:
        # reverse it 
        # return the kth element by poping from starting
        minHeap = nums[:k]
        heapq.heapify(minHeap)

        for num in nums[k:]:
            if num > minHeap[0]:
                heapq.heappushpop(minHeap, num)

        return minHeap[0]



            