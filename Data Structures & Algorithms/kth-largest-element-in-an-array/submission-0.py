class Solution:
    def findKthLargest(self, nums: List[int], k: int) -> int:
        minheap = []
        for c in nums:
            heapq.heappush(minheap, c)
            if len(minheap) > k:
                heapq.heappop(minheap)
        
        return heapq.heappop(minheap)
        