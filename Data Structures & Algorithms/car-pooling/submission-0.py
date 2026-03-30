class Solution:
    def carPooling(self, trips: List[List[int]], capacity: int) -> bool:        
        # start trips by start time
        trips.sort(key=lambda x: x[1]) 

        minHeap = [] # (end, passengers)
        current_passengers = 0

        for passengers, start, end in trips:
            # remove completed trips
            while minHeap and minHeap[0][0] <= start:
                ended_end, ended_passengers = heapq.heappop(minHeap)
                current_passengers -= ended_passengers
            
            # Add new trips
            heapq.heappush(minHeap, (end, passengers))
            current_passengers += passengers

            # capacity check
            if current_passengers > capacity:
                return False
        return True


