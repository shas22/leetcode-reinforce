class Solution:
    def resultsArray(self, nums: List[int], k: int) -> List[int]:
        n = len(nums)

        x = [1] * n

        for i in range(1, n):
            if nums[i] == nums[i - 1] + 1:

                x[i] = x[i - 1] + 1

        return [nums[i] if x[i] >= k else -1 for i in range(k - 1, n)]