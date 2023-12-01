total = 0

number_map = {
    "one": "1",
    "two": "2",
    "three": "3",
    "four": "4",
    "five": "5",
    "six": "6",
    "seven": "7",
    "eight": "8",
    "nine": "9",
}


with open("tesst.txt", "r") as f:
    for line in f:
        # index 0 = first digit seen
        # inde 1 = second digit seen
        seen = [0, 0]
        end_pos = len(line)
        for i in range(len(line) + 1):
            start_pos = i
            if i != len(line):
                # search from the left and right at the same time
                start, end = line[i], line[~i]

            # part 2 of day 1
            # check a window from the left and right of a line
            # of "number" length from the start position and end position
            for number in number_map:
                window = line[start_pos : start_pos + len(number)]
                window_reverse = line[end_pos - len(number) : end_pos]

                if window in line and not seen[0] and number_map.get(window):
                    seen[0] = number_map[window]
                if (
                    window_reverse in line
                    and not seen[1]
                    and number_map.get(window_reverse)
                ):
                    seen[1] = number_map[window_reverse]

            # part 1 day 1
            # check if the current "start" or "end" digit character has been seen already
            if not seen[0] and start.isdigit():
                seen[0] = start
            if not seen[1] and end.isdigit():
                seen[1] = end

            if seen[0] and seen[1]:
                total += int(seen[0] + seen[1])
                break

            end_pos -= 1

print(total)
