class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        if not nums:
            return 0
        
        next_unique = 1
        
        for i in range(1, len(nums)):
            if nums[i] != nums[i-1]:
                nums[next_unique] = nums[i]
                next_unique += 1
        
        return next_unique