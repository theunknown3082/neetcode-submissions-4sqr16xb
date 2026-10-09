class Solution:
    def lastStoneWeight(self, stones: List[int]) -> int:
        stoneMax = [-n for n in stones]
        heapq.heapify(stoneMax)
        while len(stoneMax) > 0:
            if len(stoneMax) == 1:
                return -heapq.heappop(stoneMax)
            a, b = -heapq.heappop(stoneMax), -heapq.heappop(stoneMax)
            a = abs(a - b)
            if a != 0:
                heapq.heappush(stoneMax, -a)
        return 0
            