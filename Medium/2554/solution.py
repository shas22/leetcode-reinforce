class Solution:
    def maxCount(self, banned: List[int], n: int, maxSum: int) -> int:
        ans = 0
        select = 0
        ban = set(banned)

        for i in range(1, n + 1):
            if select + i > maxSum:
                break

            if i not in ban:
                ans += 1
                select += i

        return ans