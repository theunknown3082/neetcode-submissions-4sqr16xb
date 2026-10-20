class Solution:
    def minCostConnectPoints(self, points: List[List[int]]) -> int:
        def manhattandist(x, y):
            return abs(x[0] - y[0]) + abs(x[1] - y[1])

        # init :
        visited = set()
        total = 0

        minheap = [(0, 0)]

        # process : 
        while minheap and len(visited) < len(points):
            cost, u = heapq.heappop(minheap)
            if u in visited:
                continue
            
            visited.add(u)
            total += cost

            for v in range(len(points)):
                if v not in visited:
                    dist = manhattandist(points[u], points[v])
                    heapq.heappush(minheap, (dist, v))
        
        return total