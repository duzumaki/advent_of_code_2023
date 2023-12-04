from collections import defaultdict

grid = []

# create grid
with open("test.txt", "r") as f:
    for line in f:
        row = []
        for line_character in line:
            if line_character == "\n":
                continue
            row.append(line_character)
        grid.append(row)

rows = len(grid)
cols = len(grid[0])


# dfs
def find_gears(row: int, col: int, number_collector: list):
    if row < 0 or col < 0 or row >= rows or col >= cols:
        return

    if grid[row][col] == ".":
        return

    if grid[row][col] == "seen":
        return

    if grid[row][col].isdigit() and grid[row][col] != "seen":
        number_collector += (grid[row][col], row, col)
        grid[row][col] = "seen"

    down = find_gears(row + 1, col, number_collector)
    up = find_gears(row - 1, col, number_collector)
    right = find_gears(row, col + 1, number_collector)
    left = find_gears(row, col - 1, number_collector)
    diag_upper_right = find_gears(row - 1, col + 1, number_collector)
    diag_upper_left = find_gears(row - 1, col - 1, number_collector)
    diag_lower_left = find_gears(row + 1, col - 1, number_collector)
    diag_lower_right = find_gears(row + 1, col + 1, number_collector)


def gear_ratios(rows: int, cols: int, gear_collector: list):
    gear_locations = set()
    gears = defaultdict(list)

    for row in range(rows):
        for col in range(cols):
            cell = grid[row][col]

            if cell == "*":
                gear_location = (row, col)
                gear_locations.add((row, col))

                find_gears(row, col, number_collector=gear_collector)

                if gear_collector:
                    gears[gear_location].append(gear_collector)
                    gear_collector = []

    grouped_numbers = defaultdict(list)

    running_gear_ratio = 0

    # i'm lazy so wasting memoery by creating all these dicts
    valid_gears = defaultdict(list)

    # this is so ugly but fuck it
    for gear, number in gears.items():
        number = number[0]
        for i in range(0, len(number), 3):
            digit, row, col = number[i], number[i + 1], number[i + 2]

            grouped_numbers[row].append((col, digit))
            # sort by col
            grouped_numbers[row].sort(key=lambda x: x[0])

        for row, col_digit in grouped_numbers.items():
            current_digits = []
            # if there's multiple numbers in the same row
            prev_col = None
            for col, digit in col_digit:
                if prev_col and (abs(prev_col - col) > 1):
                    valid_gears[gear].append(int("".join(current_digits)))
                    current_digits = []

                prev_col = col
                current_digits.append(digit)

            valid_gears[gear].append(int("".join(current_digits)))
            # reset so we don't add the same numbers to valid_gears
            grouped_numbers = defaultdict(list)

    for gear_numbers in valid_gears.values():
        product = 1
        if len(gear_numbers) != 2:
            continue
        for n in gear_numbers:
            product *= n

        running_gear_ratio += product

    return running_gear_ratio


print(gear_ratios(rows, cols, []))
