import heapq

f = open("test.txt").read().splitlines()

grid = {}

for i, row in enumerate(f):
    for j, col in enumerate(row):
        grid[(i,j)] = int(col)

def shortest_heat_path(start: tuple[int], end: tuple[int], min_steps: int, max_steps: int):
    min_heap = [(0,*start, (0,0))]
    seen = set()

    while min_heap:
        heat, row, col, dir = heapq.heappop(min_heap)

        if (row, col) == end: 
            return heat
        if (row, col, dir) in seen:
            continue

        seen.add((row, col, dir))

        for dir in {(1,0),(0,1),(-1,0),(0,-1)}-{(dir[0], dir[1]),(-dir[0],-dir[1])}:
            new_heat = heat
            new_row = row
            new_col = col
            for i  in range(1, max_steps+1):
                new_row += dir[0]
                new_col += dir[1]

                if (new_row, new_col) in grid:
                    new_heat += grid[(new_row, new_col)]

                    if i >= min_steps:
                        heapq.heappush(min_heap, (new_heat, new_row, new_col, dir))

result = shortest_heat_path((0,0),[*grid][-1], 1, 3)
print(result)
result = shortest_heat_path((0,0),[*grid][-1], 4, 10)
print(result)


            






