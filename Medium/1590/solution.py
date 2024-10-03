class Solution:
    def minSubarray(self, nums: List[int], p: int) -> int:
        total = 0
        for num in nums:
            total += num
        
        remainder = total % p
        
        if remainder == 0:
            return 0
        
        res = len(nums)

        current = 0
        
        occurence= {0: -1}
        
        current = 0
        for i, n in enumerate(nums):
            current = (current+n) % p
            prefix = (current - remainder + p) % p
            if prefix in occurence:
                length = i - occurence[prefix] 
                res = min(res,length)
            occurence[current] = i

        return -1 if res == len(nums) else res
