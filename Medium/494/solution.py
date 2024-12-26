class Solution:
    def findTargetSumWays(self, nums: List[int], S: int) -> int:
        total_sum = sum(nums)

        if (total_sum + S) % 2 != 0 or total_sum < abs(S):
            return 0

        target = (total_sum + S) // 2

        dp = [0] * (target + 1)

        dp[0] = 1

        for num in nums:
            for i in range(target, num - 1, -1):
                dp[i] += dp[i - num]

        return dp[target]