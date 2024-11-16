class Solution:
    def minimizedMaximum(self, n: int, quantities: List[int]) -> int:
        def can_distribute(max_quantity: int) -> bool:
            stores_needed = 0

            for q in quantities:
                stores_needed += (q + max_quantity - 1) // max_quantity
            return stores_needed <= n
        
        left, right = 1, max(quantities)

        while left < right:
            mid = (left + right) // 2
            
            if can_distribute(mid):
                right = mid
                
            else:
                left = mid + 1
                
        return left