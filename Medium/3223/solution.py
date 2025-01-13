class Solution:
    def minimumLength(self, s: str) -> int:
        char_counts = Counter(s)

        total = sum(2 - (count % 2) for count in char_counts.values())
        
        return total