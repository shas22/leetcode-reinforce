class Solution:
    def maxMoves(self, grid: List[List[int]]) -> int:
        
        r, c = len(grid), len(grid[0])

        unique = set(range(r))

        for i in range(c - 1):
            t = set()

            for j in unique:
                for k in range(j - 1, j + 2):

                    if 0 <= k < r and grid[j][i] < grid[k][i + 1]:
                        t.add(k)

            if not t:
                return i
            
            unique = t
            
        return c - 1