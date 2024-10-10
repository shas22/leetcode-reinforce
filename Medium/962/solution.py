from typing import List

class Solution:
    def maxWidthRamp(self, nums: List[int]) -> int:
        n = len(nums)
        stack = []
        
        for i in range(n):
            if not stack or nums[stack[-1]] > nums[i]:
                stack.append(i)
        
        max_width = 0
        for i in range(n - 1, -1, -1):
            while stack and nums[stack[-1]] <= nums[i]:
                max_width = max(max_width, i - stack.pop())
        
        return max_width