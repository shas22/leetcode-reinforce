class Solution:
    def minEnd(self, n: int, x: int) -> int:
        n -= 1
        
        result = x
        
        position = 0
        
        while n > 0:

            if not (x & (1 << position)):

                if n & 1:
                    result |= (1 << position)
                n >>= 1

            position += 1
        
        return result