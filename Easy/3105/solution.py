class Solution:
    def longestMonotonicSubarray(self, nums: List[int]) -> int:
        if not nums:
            return 0
        def find_longest_sequence(nums, comparison_func):
            current_length = 1
            max_length = 1
            
            for i in range(1, len(nums)):
                if comparison_func(nums[i-1], nums[i]):
                    current_length += 1
                    max_length = max(max_length, current_length)
                else:
                    current_length = 1
                    
            return max_length
        
        increasing_length = find_longest_sequence(nums, lambda x, y: x < y)
        decreasing_length = find_longest_sequence(nums, lambda x, y: x > y)
        return max(increasing_length, decreasing_length)