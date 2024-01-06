f = open("test.txt").read().splitlines()

polygon_coords = [(0,0)]

current = [0,0]
b = 0

DIRECTION = {
    "0": "R",
    "1": "D",
    "2": "L",
    "3": "U"
}

for line in f:
    _, _, color = line.split()
    color = color[2:-1]
    direction = DIRECTION[color[-1]]
    distance = int(color[:-1], 16)

    b += distance

    if direction == "L":
        current[1] += -distance
        polygon_coords.append(tuple(current))
    elif direction == "R":
        current[1] += distance
        polygon_coords.append(tuple(current))
    elif direction == "U":
        current[0] += -distance
        polygon_coords.append(tuple(current))
    elif direction == "D":
        current[0] += distance
        polygon_coords.append(tuple(current))


column1 = 0
column2 = 0
border_coord_count = 0

# shoe lace (https://www.youtube.com/watch?v=FSWPX0XB7a0)
for i in range(len(polygon_coords)-1):
    current_coord, next_coord = polygon_coords[i], polygon_coords[i+1]
    column1 += current_coord[0] * next_coord[1]
    column2 += current_coord[1] * next_coord[0]


A = abs(column1-column2) /2

# pick's theorem (https://en.wikipedia.org/wiki/Pick%27s_theorem)
i = A-b // 2 +1
print(i+b)