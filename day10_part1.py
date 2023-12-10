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

    # unlike the solution above we need to add "S" in our check
    # since we're following the pipe along it's valid loop rather than checking
    # every direction blindly

    # if we came from down, (the start of a pipe) what accepts the end of the pipe,
    if cell in "S|7F" and grid[row + 1][col] in "|JL" and (row + 1, col) not in seen:
        coord = (row + 1, col)
        q.append(coord)
        seen.add(coord)

    # if we came from up, (the start of a pipe) what accepts the end of the pipe
    if cell in "S|JL" and grid[row - 1][col] in "|F7" and (row - 1, col) not in seen:
        coord = (row - 1, col)
        q.append(coord)
        seen.add(coord)

    # if we came from left, (the start of a pipe) what accepts the end of the pipe
    if cell in "S-J7" and grid[row][col - 1] in "-LF" and (row, col - 1) not in seen:
        coord = (row, col - 1)
        q.append(coord)
        seen.add(coord)

    # if we came from right, (the start of a pipe) what accepts the end of the pipe
    if cell in "S-FL" and grid[row][col + 1] in "-7J" and (row, col + 1) not in seen:
        coord = (row, col + 1)
        q.append(coord)
        seen.add(coord)


print(len(seen) // 2)


# the below solution didn't take into account you can only certain directions if you entered 
# a pipe. e.g 7 -> J works but not 7 -> F.
# it was just checking all 4 directions and going through pipes it shouln't have been allowed
# to traverse though.

# directions = ((0, 1), (1, 0), (-1, 0), (0, -1))

# # ((pipe_end_1 x, y), (pipe_end_2 x, y))
# PIPE_ENDS = {
#     "|": ((1, 0), (-1, 0)),
#     "-": ((0, 1), (0, -1)),
#     "L": ((-1, 0), (0, 1)),
#     "J": ((-1, 0), (0, -1)),
#     "F": ((1, 0), (0, 1)),
#     "7": ((1, 0), (0, -1)),
# }

# def other_pipe_end(pipe_type: str, came_from: tuple, row: int, col: int):
#     pipe_ends = PIPE_ENDS[pipe_type]
#     pipe_end1, pipe_end2 = pipe_ends[0], pipe_ends[1]

#     if (
#         row + pipe_end1[0] < 0
#         or row + pipe_end1[0] >= ROWS
#         or col + pipe_end1[1] < 0
#         or col + pipe_end1[1] >= COLS
#     ):
#         return None

#     if (
#         row + pipe_end2[0] < 0
#         or row + pipe_end2[0] >= ROWS
#         or col + pipe_end2[1] < 0
#         or col + pipe_end2[1] >= COLS
#     ):
#         return None

#     if came_from == pipe_end1:
#         return grid[row + pipe_end2[0]][col + pipe_end2[1]], pipe_end2[0], pipe_end2[1]

#     return grid[row + pipe_end1[0]][col + pipe_end1[1]], pipe_end1[0], pipe_end1[1]


# while q:
#     row, col = q.popleft()


#     for r, c in directions:
#         new_row = row + r
#         new_col = col + c

#         if new_row < 0 or new_col < 0 or new_row >= ROWS or new_col >= COLS:
#             continue
#         if grid[new_row][new_col] == ".":
#             continue
#         if (new_row, new_col) in seen:
#             continue

#         if grid[new_row][new_col] in PIPE_ENDS:
#             pipe_type = grid[new_row][new_col]

#             came_from = row - new_row, col - new_col

#             other_end = other_pipe_end(pipe_type, came_from, new_row, new_col)

#             if other_end is None:
#                 continue

#             pipe_end, p_row, p_col = other_end

#             # if we came from the left, (the start of a pipe) what accets the end of the pipe
#             if came_from == (0, -1) and pipe_type in "-J7" and pipe_end in "-LF":
#                 q.append((new_row + p_row, new_col + p_col))
#                 seen.add((new_row + p_row, new_col + p_col))

#             # if we came from the right, (the start of a pipe) what accets the end of the pipe
#             if came_from == (0, 1) and pipe_type in "-LF" and pipe_end in "-7J":
#                 q.append((new_row + p_row, new_col + p_col))
#                 seen.add((new_row + p_row, new_col + p_col))

#             # if we came from down, (the start of a pipe) what accepts the end of the pipe
#             if came_from == (1, 0) and pipe_type in "|7F" and pipe_end in "|JL":
#                 q.append((new_row + p_row, new_col + p_col))
#                 seen.add((new_row + p_row, new_col + p_col))

#             # if we came from up, (the start of a pipe) what accepts the end of the pipe
#             if came_from == (-1, 0) and pipe_type in "|LJ" and pipe_end in "|7F":
#                 q.append((new_row + p_row, new_col + p_col))
#                 seen.add((new_row + p_row, new_col + p_col))

#         q.append((new_row, new_col))