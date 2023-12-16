f = open("test.txt").readlines()

grid = ()
for line in f:
    grid += (line[:-1],)

ROWS = len(grid)


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

length = 0

while True:
    length += 1
    washing_machine_cycle()

    if grid in seen:
        break
    seen.add(grid)
    grid_states_in_order.append(grid)


cycle_start = grid_states_in_order.index(grid)


"""
[] = grid state
X = grid states in loop
0 = cycle start


->[i]->[i]->O->\
            X   X
            |   |
            X-X/

1_000_000_000 - cycle_start doing this 
this is the 1 billion cycles we care about minus the start

we divide it length-cycle_start 
because length actually includes the ->[i]->[i] part and we only want the 
actual cycle length when doing our calculation

so the cycle part is just length - cycle_start = x

so it's how many times do we go around a cycle of size x. 1 billion / x = y remainder z
we onyly care about the remainder z because want to know which grid state did we land on 
when we hit the 1 billionith cycle. 

+cycle_start is added back because once we calculte the correct position in the cycle
we need to add the ->[i]->[i] part back since those are the grid state steps before the cycle started.

"""
grid = grid_states_in_order[(1_000_000_000 - cycle_start) % (length - cycle_start) + cycle_start]


TOTAL_LOAD = 0

for i, row in enumerate(grid):
    rounded_rock_count = 0 

    for col in row:
        if col == "O":
            rounded_rock_count += 1

    TOTAL_LOAD += rounded_rock_count * (ROWS - i)

print(TOTAL_LOAD)
