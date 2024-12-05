class Solution:
    def canChange(self, start: str, target: str) -> bool:
        if start.replace('_', '') != target.replace('_', ''):
            return False
        
        start_positions = [(i, char) for i, char in enumerate(start) if char != '_']
        target_positions = [(i, char) for i, char in enumerate(target) if char != '_']
        
        for (start_idx, start_char), (target_idx, target_char) in zip(start_positions, target_positions):
            if start_char == 'L' and start_idx < target_idx:
                return False

            if start_char == 'R' and start_idx > target_idx:
                return False
        
        return True