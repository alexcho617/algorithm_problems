
def dfs(i, j, grid):
    if i < 0 or j < 0 or i >= row or j >= col or grid[i][j] == 0:
        return
    grid[i][j] = 0  # Mark cell as zero to avoid recounting
    dfs(i + 1, j, grid)
    dfs(i - 1, j, grid)
    dfs(i, j + 1, grid)
    dfs(i, j - 1, grid)
    return
    islands = 0
    row = len(grid)
    col = len(grid[0])
    for i in range(0, row):  # Traverse grid
        for j in range(0, col):
            if grid[i][j] == 1:
                dfs(i, j, grid)
                islands += 1
    return islands


mat = [[1, 1, 1], [1, 0, 0], [1, 0, 1]]
print('Number of Islands : ', dfs(mat))
