from collections import deque

grid = []

f = open("test.txt", "r")

# create grid
for line in f:
    row = [c for c in line if c != "\n"]
    grid.append(row)


ROWS = len(grid)
COLS = len(grid[0])


def find_s_starting_coord(grid):
    for row in range(ROWS):
        for col in range(COLS):
            if grid[row][col] == "S":
                return row, col


S_START_COORD = find_s_starting_coord(grid)
seen = set({S_START_COORD})
q = deque([S_START_COORD])


while q:
    row, col = q.popleft()
    cell = grid[row][col]

    if row < 0 or col < 0 or row >= ROWS or col >= COLS:
        continue

    if cell in "S|7F" and grid[row + 1][col] in "|JL" and (row + 1, col) not in seen:
        coord = (row + 1, col)
        q.append(coord)
        seen.add(coord)

    if cell in "S|JL" and grid[row - 1][col] in "|F7" and (row - 1, col) not in seen:
        coord = (row - 1, col)
        q.append(coord)
        seen.add(coord)

    if cell in "S-J7" and grid[row][col - 1] in "-LF" and (row, col - 1) not in seen:
        coord = (row, col - 1)
        q.append(coord)
        seen.add(coord)

    # if we came from right, (the start of a pipe) what accepts the end of the pipe
    if cell in "S-FL" and grid[row][col + 1] in "-7J" and (row, col + 1) not in seen:
        coord = (row, col + 1)
        q.append(coord)
        seen.add(coord)

print(len(seen)//2)

def count_polygon_edges_hit(row: int, col: int):
    row_line = grid[row]
    count = 0
    for c in range(col):
        # seen is the loop coords itself
        # so ignore that as we're trying to count to point
        # that's either inside or outside of the loop
        if (row, c) not in seen:
            continue
        count += row_line[c] in ("F", "7", "|")

    return count


enclosed_in_loop_count = 0
for row in range(ROWS):
    for col in range(COLS):
        
        if (row, col) in seen:
            continue
        count = count_polygon_edges_hit(row, col)

        if count and count % 2 == 1:
            enclosed_in_loop_count += 1

print(enclosed_in_loop_count)
