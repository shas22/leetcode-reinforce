class Solution:
    def maxScore(self, s: str) -> int:
        l = 0
        
        r = s.count("1")

        ans = 0

        for i in s[:-1]:
            l += int(i) ^ 1

            r -= int(i)

            ans = max(ans, l + r)

        return ans