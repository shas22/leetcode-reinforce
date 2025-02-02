class Solution:
    def check(self, nums: List[int]) -> bool:
        for i in range(1, len(nums)):
            if nums[i-1] > nums[i]:
                return nums[-1] <= nums[0] and nums[i:] == sorted(nums[i:])
                
        return True