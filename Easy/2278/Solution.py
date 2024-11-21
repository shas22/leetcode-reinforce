class Solution:
    def percentageLetter(self, s: str, letter: str) -> int:
        letter_count = 0
        for char in s:
            if char == letter:
                letter_count += 1

        percentage = letter_count * 100 // len(s)
        
        return percentage