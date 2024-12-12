class Solution:
    def maximumBeauty(self, nums: List[int], k: int) -> int:
        max_range = max(nums) + k * 2 + 2

        frequency = [0] * max_range

        for num in nums:
            frequency[num] += 1

            frequency[num + k * 2 + 1] -= 1
            
        return max(accumulate(frequency))