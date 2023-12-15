f = open("test.txt").read().split("\n\n")


output = 0

def get_mirror_diff(grid, mirror_diff = 0):
    global output

    for row in range(1, len(grid)):
        top = grid[:row][::-1]
        bottom = grid[row:]
        row_diff = 0

        for x, y in zip(top, bottom):
            for a,b in zip(x, y):
                if a != b:
                    row_diff += 1

        if row_diff == 1:
            mirror_diff += 1

        if mirror_diff == 1:
            return row
    return 0

for grid_string in f:
    grid = []
    grid.extend(grid_string.strip().split("\n"))

    output += 100 * get_mirror_diff(grid)

    transposed_grid = tuple(zip(*grid))

    output += get_mirror_diff(transposed_grid)

print(output)
