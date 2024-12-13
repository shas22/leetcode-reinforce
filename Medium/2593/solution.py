class Solution:
    def findScore(self, nums: List[int]) -> int:
        indexed_nums = sorted((num, idx) for idx, num in enumerate(nums))

        marked = [False] * len(nums)
        total_score = 0
        
        for value, index in indexed_nums:
            if marked[index]:
                continue

            total_score += value

            marked[index] = True
            if index > 0:
                marked[index - 1] = True
            if index < len(nums) - 1:
                marked[index + 1] = True
        
        return total_score