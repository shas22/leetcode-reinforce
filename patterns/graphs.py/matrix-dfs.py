def dfs(grid, r, c, visited):
    rows = len(grid)
    cols = len(grid[0]) # applicable when r x c is square

    if min(r,c) < 0 or r == rows or c == cols or (r,c) in visited or grid[r][c] ==1:
        return 0

    if r == rows - 1 and c == cols - 1:
        return 1

    visit.add((r,c))

    count = 0

    count = 0
    count += dfs(grid, r + 1, c, visit)
    count += dfs(grid, r - 1, c, visit)
    count += dfs(grid, r, c + 1, visit)
    count += dfs(grid, r, c - 1, visit)

    visit.remove((r, c))
    return count   
