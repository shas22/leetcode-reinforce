class Solution:
    def longestSquareStreak(self, nums: List[int]) -> int:
        s = set(nums)

        res = -1

        for sbs in nums:
            t = 0

            while sbs in s:
                sbs *= sbs
                t += 1

            if t > 1:
                res = max(res, t)

        return res