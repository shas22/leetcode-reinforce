class Solution:
    def countBadPairs(self, nums: List[int]) -> int:
        count = Counter()
        res = 0
        for i, x in enumerate(nums):
            res += i - count[i - x]
            count[i - x] += 1
            
        return res