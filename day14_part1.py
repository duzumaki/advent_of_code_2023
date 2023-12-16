f = open("test.txt", "r").readlines()



min_row_available_for_col = []
grid = []

for line in f:
    grid.append([c for c in line if c != "\n"])

ROWS = len(grid)
COLS = len(grid[0])

def dfs(row, col):
    if row < 0:
        grid[row+1][col] = "0"
        return

    if grid[row][col] in ("#", "0"):
        grid[row+1][col] = "0"
        return
    
    # go up
    dfs(row-1, col)



for row in range(ROWS):
    for col in range(COLS):
        if grid[row][col] == "O":
            grid[row][col] = "."
            dfs(row, col)

print(grid)

TOTAL_LOAD = 0

for i, row in enumerate(grid):
    rounded_rock_count = 0

    for col in row:
        if col == "0":
            rounded_rock_count += 1
    
    TOTAL_LOAD += rounded_rock_count  * (ROWS-i)

print(TOTAL_LOAD)
