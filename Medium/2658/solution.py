class Solution:
    def findMaxFish(self, grid: List[List[int]]) -> int:
        def dfs(i: int, j: int) -> int:
            count = grid[i][j]
            grid[i][j] = 0

            for a, b in pairwise((-1, 0, 1, 0, -1)):
                x = i + a
                y = j + b
                if 0 <= x < m and 0 <= y < n and grid[x][y]:
                    count += dfs(x, y)

            return count

        m, n = len(grid), len(grid[0])
        res = 0

        for i in range(m):
            for j in range(n):
                if grid[i][j]:
                    res = max(res, dfs(i, j))

        return res