class Solution:
    def countSquares(self, matrix: List[List[int]]) -> int:
        prev_row = None
        
        s = 0

        for row in matrix:
            prev_x = None

            for i, x in enumerate(row):

                if x == 0:
                    prev_x = x
                    continue

                if prev_x and prev_row:
                    x = row[i] = min(prev_row[i - 1], prev_row[i], prev_x) + 1

                s += x
                prev_x = x

            prev_row = row
        return s