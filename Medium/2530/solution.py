class Solution:
    def maxKelements(self, nums: List[int], k: int) -> int:
        result = 0

        maximum = [-n for n in nums]

        heapq.heapify(maximum)

        while k:
            n = -heapq.heappop(maximum)
            result += n 
            k -= 1
            heapq.heappush(maximum, -math.ceil(n/3))


        return result