class Solution:
    def findPermutationDifference(self, source_string: str, target_string: str) -> int:
        char_to_position = {}

        for position, character in enumerate(source_string):
            char_to_position[character] = position

        total_difference = 0
        for current_position, character in enumerate(target_string):
            original_position = char_to_position[character]
            total_difference += abs(original_position - current_position)
            
        return total_difference