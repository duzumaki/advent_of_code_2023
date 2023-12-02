LIMITS = {"red": 12, "green": 13, "blue": 14}

game_id_total = 0

with open("test.txt", "r") as f:
    for line in f:
        game_no, picks = line.split(":")
        # game 1 -> 1
        game_no = int(game_no.split()[1])

        elf_picked_cubes_in_current_game = picks.split(";")
        limit_broken = False

        # e.g [' 19 blue, 12 red', ' 19 blue, 2 green, 1 red', ' 13 red, 11 blue\n']
        for pick in elf_picked_cubes_in_current_game:
            pick = pick.split(",")
            number = ""
            color = ""
            # e.g 19 blue
            for individual_color_pick in pick:
                individual_color_pick.strip()

                for i in range(len(individual_color_pick) - 1):
                    # 19
                    if individual_color_pick[i].isdigit():
                        number += individual_color_pick[i]
                    # blue
                    if individual_color_pick[i + 1].isalpha():
                        color = individual_color_pick[i + 1 :]
                        break

                if int(number) > LIMITS[color.strip()]:
                    limit_broken = True
                    break

                number = ""
                color = ""

            if limit_broken is True:
                break

        if limit_broken is False:
            game_id_total += game_no

print(game_id_total)
