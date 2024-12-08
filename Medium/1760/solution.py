class Solution:
    def minimumSize(self, nums: List[int], maxOperations: int) -> int:
        def check(mx: int) -> bool:
            operations_needed = sum((x - 1) // mx for x in nums)
            
            return operations_needed <= maxOperations
        return bisect_left(range(1, max(nums)), True, key=check) + 1