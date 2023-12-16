f = open("test.txt").readlines()

grid = ()
for line in f:
    grid += (line[:-1],)

ROWS = len(grid)

print(grid)

def washing_machine_cycle():
    """
    to rotate a matrix by 90 degrees to the right.

    for 90 degrees rotation:
       
            zip(*grid) reverse rows
                         W
    1----2    1---3    3----1
   W|    | -> |   | -> |    |
    3----4    2---4    4----2

    """
    global grid

    global grid
    for _ in range(4):
        grid = tuple(map("".join, zip(*grid)))

        new_rows = []
        for row in grid:
            tilted_row = []
            for group in row.split("#"):
                tilted_row.append("".join(sorted(tuple(group), reverse=True)))
            new_rows.append("#".join(tilted_row))

        grid = new_rows

        grid = tuple(row[::-1] for row in grid)



seen = {grid}
grid_states_in_order = [grid]

cycle_length = 0

while True:
    cycle_length += 1
    washing_machine_cycle()

    if grid in seen:
        break
    seen.add(grid)
    grid_states_in_order.append(grid)


cycle_start = grid_states_in_order.index(grid)


grid = grid_states_in_order[(1_000_000_000 - cycle_start) % (cycle_length - cycle_start) + cycle_start]


TOTAL_LOAD = 0

for i, row in enumerate(grid):
    rounded_rock_count = 0 

    for col in row:
        if col == "O":
            rounded_rock_count += 1

    TOTAL_LOAD += rounded_rock_count * (ROWS - i)

print(TOTAL_LOAD)
