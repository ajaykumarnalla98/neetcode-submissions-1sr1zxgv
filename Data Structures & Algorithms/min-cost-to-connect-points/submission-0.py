class Solution:
    def minCostConnectPoints(self, points: List[List[int]]) -> int:
        n = len(points)

        visited = [False] * n
        minHeap = [(0, 0)]
        total_cost = 0
        edges_used = 0

        while edges_used < n:
            cost, u = heapq.heappop(minHeap)

            if visited[u]:
                continue
            visited[u] = True
            total_cost += cost
            edges_used += 1

            for v in range(n):
                if not visited[v]:
                    x1, y1 = points[u]
                    x2, y2 = points[v]
                    distance = abs(x1-x2) + abs(y1-y2)
                    heapq.heappush(minHeap, (distance, v))

        return total_cost            




        