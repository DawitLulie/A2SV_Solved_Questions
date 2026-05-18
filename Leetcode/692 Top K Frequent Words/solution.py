from collections import Counter
import heapq

class Solution:
    def topKFrequent(self, words: List[str], k: int) -> List[str]:
        freq = Counter(words)

        heap = []

        for word, count in freq.items():
            # push negative frequency for max behavior
            heapq.heappush(heap, (-count, word))

        result = []

        for _ in range(k):
            count, word = heapq.heappop(heap)
            result.append(word)

        return result