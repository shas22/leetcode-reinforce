class Solution:
    def titleToNumber(self, columnTitle: str) -> int:
        res = 0

        for c in map(ord, columnTitle):
            res = res * 26 + c - ord("A") + 1

        return res