class Solution:
    def arrangeCoins(self, n: int) -> int:
        start = 1
        end = n

        while start <= end:
            mid = start + (end - start) // 2
            total = mid * (mid + 1) // 2
            
            if total == n:
                return mid
            elif total < n:
                start = mid + 1
            else:
                end = mid - 1

        return end