class Solution:
    def numJewelsInStones(self, jewels: str, stones: str) -> int:
        jset = set(jewels)

        count = sum(char in jset for char in stones)

        return count