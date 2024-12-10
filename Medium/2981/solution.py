from collections import defaultdict
from typing import Dict

class Solution:
    def maximumLength(self, s: str) -> int:
        def is_substring_repeating(substring_length: int) -> bool:
            substring_counts: Dict[str, int] = defaultdict(int)
            
            current_index = 0
            while current_index < sequence_length:
                end_index = current_index + 1
                while end_index < sequence_length and s[end_index] == s[current_index]:
                    end_index += 1

                substring_counts[s[current_index]] += max(0, end_index - current_index - substring_length + 1)
                
                current_index = end_index
            
            return max(substring_counts.values()) >= 3

        sequence_length = len(s)
        
        left_bound, right_bound = 0, sequence_length
        while left_bound < right_bound:
            mid_point = (left_bound + right_bound + 1) >> 1

            if is_substring_repeating(mid_point):
                left_bound = mid_point
            else:
                right_bound = mid_point - 1
        
        return -1 if left_bound == 0 else left_bound