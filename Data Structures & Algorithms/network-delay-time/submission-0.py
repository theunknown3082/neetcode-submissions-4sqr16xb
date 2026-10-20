class Solution:
    def networkDelayTime(self, times: List[List[int]], n: int, k: int) -> int:
        
        # init :
        adj = [[] for _ in range(n + 1)]
        for u, v, w in times:
            adj[u].append((v, w))

        dist = [float("inf")] * (n + 1)
        dist[k] = 0

        # prep :
        minheap = [(0, k)]

        # process :
        while minheap:
            d, u = heapq.heappop(minheap)

            if d > dist[u]:
                continue
            
            for v, weight in adj[u]:
                if d + weight < dist[v]:
                    dist[v] = d + weight
                    heapq.heappush(minheap, (dist[v], v))

        return max(dist[1:]) if max(dist[1:]) != float("inf") else -1