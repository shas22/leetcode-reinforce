class Solution:
    def canSortArray(self, nums: List[int]) -> bool:
        prev_group_max = 0
        
        curr_idx, length = 0, len(nums)
        
        while curr_idx < length:
            current_bit_count = nums[curr_idx].bit_count()
            next_idx = curr_idx + 1
            group_min = group_max = nums[curr_idx]
            
            while next_idx < length and nums[next_idx].bit_count() == current_bit_count:
                group_min = min(group_min, nums[next_idx])

                group_max = max(group_max, nums[next_idx])

                next_idx += 1
            
            if prev_group_max > group_min:
                return False
                
            prev_group_max = group_max
            curr_idx = next_idx
            
        return True