class Solution:
    def coloredCells(self, n: int) -> int:
        count = 1
        jump = 4

        while n > 1:
            count += jump
            jump += 4
            n -= 1
            
        return count