class Solution:
    def maxTwoEvents(self, events: List[List[int]]) -> int:
        events.sort(key=lambda x: x[0])
        
        max_values = [0] * (len(events) + 1)
        max_values[len(events)] = 0
        
        for i in range(len(events) - 1, -1, -1):
            max_values[i] = max(max_values[i + 1], events[i][2])

        max_total_value = 0

        for start, end, value in events:
            next_event_index = bisect_right(events, end, key=lambda x: x[0])
            
            current_total = value
            if next_event_index < len(events):
                current_total += max_values[next_event_index]
            
            max_total_value = max(max_total_value, current_total)
        
        return max_total_value