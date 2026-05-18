import heapq

class Solution:
    def kthSmallest(self, matrix, k):
        n = len(matrix)

        heap = []

        for i in range(n * n):
            row = i // n
            col = i % n

            heapq.heappush(heap, -matrix[row][col])

            if len(heap) > k:
                heapq.heappop(heap)

        return -heap[0]