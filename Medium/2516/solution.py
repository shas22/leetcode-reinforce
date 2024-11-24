class Solution:
    def takeCharacters(self, s: str, k: int) -> int:
        frequency = Counter(s)

        if any(frequency[c] < k for c in "abc"):
            return -1

        longest_length = j = 0

        for current_index, character in enumerate(s):
            frequency[character] -= 1

            while frequency[character] < k:
                frequency[s[j]] += 1
                j += 1

            longest_length = max(longest_length, current_index - j + 1)
            
        return len(s) - longest_length