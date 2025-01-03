class Solution:
    def waysToSplitArray(self, nums: List[int]) -> int:
        rightsum = sum(nums)
        left = 0 

        ans = 0

        for i in range(len(nums) - 1):
            left += nums[i]

            rightsum -= nums[i]

            if left >= rightsum:
                ans += 1
                
        return ans