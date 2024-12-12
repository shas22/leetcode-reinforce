import heapq
import math

class Solution:
    def pickGifts(self, gifts: list[int], k: int) -> int:
        heap = [-gift for gift in gifts]
        heapq.heapify(heap)

        for _ in range(k):
            largest_gift = -heapq.heappop(heap)

            root = math.floor(math.sqrt(largest_gift))
            
            heapq.heappush(heap, -root)

        return -sum(heap)