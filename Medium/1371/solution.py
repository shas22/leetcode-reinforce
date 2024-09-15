class Solution:
    def findTheLongestSubstring(self, s: str) -> int:
        # Dictionary to map vowel counts to binary representation
        vowels = {'a': 1, 'e': 2, 'i': 4, 'o': 8, 'u': 16}
        # To store the first occurrence of each vowel state
        state = 0
        # Initialize with -1 to cover edge cases like entire string being valid
        state_to_index = {0: -1}
        max_len = 0
        
        # Iterate over each character in the string
        for i, char in enumerate(s):
            # If the character is a vowel, flip its corresponding bit in the state
            if char in vowels:
                state ^= vowels[char]
            
            # If this state has been seen before, calculate the possible length
            if state in state_to_index:
                max_len = max(max_len, i - state_to_index[state])
            else:
                state_to_index[state] = i
        
        return max_len
