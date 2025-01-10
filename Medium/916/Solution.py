class Solution:
    def wordSubsets(self, words1: List[str], words2: List[str]) -> List[str]:

        required_char_frequencies = {}
        

        for target_word in words2:

            for char in target_word:

                current_char = target_word.count(char)
                

                previous_max = required_char_frequencies.get(char, 0)
                required_char_frequencies[char] = max(current_char, previous_max)
        

        valid_words = []
        
        for found_word in words1:
            is_valid = True
            
            for required_char, required_count in required_char_frequencies.items():
                actual_count = found_word.count(required_char)
                
                if actual_count < required_count:
                    is_valid = False
                    break
            
            if is_valid:
                valid_words.append(found_word)
        
        return valid_words