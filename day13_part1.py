f = open("test.txt").read().split("\n\n")


output = 0

for grid_string in f:
    print(grid_string)
    print()
    grid = []
    grid.extend(grid_string.strip().split("\n"))

    for row in range(1, len(grid)):
        # top is a mirror of the bottom
        top = grid[:row][::-1]
        bottom = grid[row:]

        top = top[: len(bottom)]
        bottom = bottom[: len(top)]

        if top == bottom:
            output += row * 100

    transposed_grid = tuple(zip(*grid))

    for col in range(1, len(transposed_grid)):
        # the grid is transposed now so top is actually
        # the left
        top = transposed_grid[:col][::-1]
        bottom = transposed_grid[col:]

        top = top[: len(bottom)]
        bottom = bottom[: len(top)]

        if top == bottom:
            output += col


print(output)
