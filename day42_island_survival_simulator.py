def dfs(grid, row, col):
    rows = len(grid)
    cols = len(grid[0])

    if (
        row < 0 or
        col < 0 or
        row >= rows or
        col >= cols or
        grid[row][col] == "0"
    ):
        return

    grid[row][col] = "0"

    dfs(grid, row + 1, col)
    dfs(grid, row - 1, col)
    dfs(grid, row, col + 1)
    dfs(grid, row, col - 1)

def num_islands(grid):
    if not grid:
        return 0

    count = 0
    rows = len(grid)
    cols = len(grid[0])

    for r in range(rows):
        for c in range(cols):
            if grid[r][c] == "1":
                count += 1
                dfs(grid, r, c)
    return count

grid = [
    ["1", "1", "0", "0", "0"],
    ["1", "1", "0", "0", "0"],
    ["0", "0", "1", "0", "0"],
    ["0", "0", "0", "1", "1"]
]

result = num_islands(grid)
print("Number of Islands:", result)