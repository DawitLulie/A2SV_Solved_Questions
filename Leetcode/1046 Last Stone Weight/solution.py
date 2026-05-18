import heapq
class Solution:
    def lastStoneWeight(self, nums: List[int]) -> int:
        heap = []
        for num in nums:
            heapq.heappush(heap, -num)
        
        while len(heap) > 1:
            x = -heapq.heappop(heap)
            y = -heapq.heappop(heap)

            if x != y:
                heapq.heappush(heap, -(x-y))
    
        return -heap[0] if heap else 0
        