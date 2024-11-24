class Solution:
    def maxMatrixSum(self, matrix: List[List[int]]) -> int:
        total = negative_count = 0

        min_absolute = inf

        for current_row in matrix:
            for element in current_row:
                total += abs(element)

                min_absolute = min(min_absolute, abs(element))

                if element < 0:
                    negative_count += 1

        if negative_count % 2 == 0 or min_absolute == 0:
            return total
            
        return total - min_absolute * 2