f = open("test.txt").read().splitlines()

grid = {}

# start on left col, to go a right col
# (pos, dir)


for j, row in enumerate(f):
    for i, col in enumerate(row):
        # here row is the real and col is the img part
        grid[complex(i, j)] = col


def energize(start: int, direction: int):
    seen = set()
    q = [(start, direction)]

    while q:
        pos, dir = q.pop()
        while (pos, dir) not in seen:
            seen.add((pos, dir))
            pos += dir

            if grid.get(pos) == "|":
                dir = 1j
                q.append((pos, -dir))
            elif grid.get(pos) == "-":
                dir = -1
                q.append((pos, -dir))
            elif grid.get(pos) == "/":
                # reflect along the diagonal and take the negative because
                # this is a movement from left -> / -> up (think of it as flipped L)
                # and vice versa
                dir = -complex(dir.imag, dir.real)

            elif grid.get(pos) == "\\":
                # reflect along the diagonal
                # this is a movement from right -> \ -> up (think of an L)
                # and vice versa
                dir = complex(dir.imag, dir.real)

            elif grid.get(pos) is None:
                break

    return len(set(pos for pos, _ in seen)) - 1


best = 0

for pos in grid:
    for direction in (1, -1, 1j, -1j):
        if pos - direction in grid:
            continue

        best = max(best, energize(pos - direction, direction))

print(best)
