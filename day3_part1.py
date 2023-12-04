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
def find_number(row: int, col: int, number_collector: list, search_diag: bool = False):
    if row < 0 or col < 0 or row >= rows or col >= cols:
        return

    if grid[row][col] == ".":
        return

    if grid[row][col] == "seen":
        return


    if grid[row][col].isdigit() and grid[row][col] != "seen":
        number_collector += (grid[row][col], row, col)
        grid[row][col] = "seen"

    down = find_number(row + 1, col, number_collector)
    up = find_number(row - 1, col, number_collector)
    right = find_number(row, col + 1, number_collector)
    left = find_number(row, col - 1, number_collector)

    if search_diag:
        diag_upper_right = find_number(
            row - 1,
            col + 1,
            number_collector,
        )
        diag_upper_left = find_number(row - 1, col - 1, number_collector)
        diag_lower_left = find_number(row + 1, col - 1, number_collector)
        diag_lower_right = find_number(row + 1, col + 1, number_collector)


def grid_pass(rows: int, cols: int, search_diag: False, number_collector: list):
    global output
    numbers = []
    for row in range(rows):
        for col in range(cols):
            cell = grid[row][col]

            if not cell.isalnum() and cell != ".":
                find_number(
                    row,
                    col,
                    number_collector=number_collector,
                    search_diag=search_diag,
                )
                if number_collector:
                    numbers.append(number_collector)
                    number_collector = []

    output = []
    grouped_numbers = defaultdict(list)

    for number in numbers:
        for i in range(0, len(number), 3):
            digit, row, col = number[i], number[i + 1], number[i + 2]

            grouped_numbers[row].append((col, digit))

    numbers_in_correct_order = []
    # sort by column position
    for row in grouped_numbers:
        current_numbers = []
        prev_col = None
        for col_digit in sorted(grouped_numbers[row], key=lambda x: x[0]):
            col, digit = col_digit

            if prev_col and (abs(prev_col - col) > 1):
                numbers_in_correct_order.append(int("".join(current_numbers)))
                current_numbers = []

            prev_col = col
            current_numbers.append(digit)
        numbers_in_correct_order.append(int("".join(current_numbers)))

    return numbers_in_correct_order


# pass 1
# collect the numbers then mark the grid to mark all up, down, right, left touching
# symbol numbers as seen
pass1 = grid_pass(rows, cols, search_diag=False, number_collector=[])


# pass 2
# collect the numbers then mark the grid to mark all up, down, right, left touching
# symbol numbers as seen
pass2 = grid_pass(rows, cols, search_diag=True, number_collector=[])

