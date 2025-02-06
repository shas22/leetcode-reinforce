from typing import List
from collections import defaultdict

class Solution:
    def tupleSameProduct(self, nums: List[int]) -> int:
        product_counts = defaultdict(int)
        
        for i in range(len(nums)):
            for j in range(i):
                product = nums[i] * nums[j]
                product_counts[product] += 1

        total_combinations = 0
        for count in product_counts.values():
            if count >= 2:
                total_combinations += count * (count - 1) // 2
        
        return total_combinations * 8