class Solution:
    def maxEqualRowsAfterFlips(self, matrix: List[List[int]]) -> int:
        patterns = Counter()
        for current_row in matrix:
            normalized = tuple(current_row) if current_row[0] == 0 else tuple(bit ^ 1 for bit in current_row)
            patterns[normalized] += 1
        return max(patterns.values())