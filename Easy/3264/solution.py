class Solution:
    def continuousSubarrays(self, nums: List[int]) -> int:
        total_count = 0

        left = 0

        max_window = deque()

        min_window = deque()
        
        for right in range(len(nums)):
            while max_window and nums[max_window[-1]] < nums[right]:
                max_window.pop()

            max_window.append(right)
            
            while min_window and nums[min_window[-1]] > nums[right]:
                min_window.pop()

            min_window.append(right)
            
            while max_window and min_window and nums[max_window[0]] - nums[min_window[0]] > 2:
                left += 1
                
                if max_window[0] < left:
                    max_window.popleft()
                if min_window[0] < left:
                    min_window.popleft()
            
            total_count += right - left + 1
        
        return total_count