class Solution:
    def maxArea(self, heights: List[int]) -> int:
        # we need a tracker to keep track of the current biggest product of index and between 2 heights
        # whichever lower is used for distance x height 
        # if equal move either one
        l, r = 0, len(heights) - 1
        res = 0

        while l < r:
            res = max(res, min(heights[l], heights[r]) * (r - l))
            if heights[l] < heights[r]:
                l += 1
            elif heights[r] <= heights[l]:
                r -= 1
            
        return res