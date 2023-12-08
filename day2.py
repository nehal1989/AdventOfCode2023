import re

# create function to read in file
file_name = "day_2_input_test.txt"
file_name = "day_2_input.txt"
def read_input_file(file_name: str):
    with open(file_name) as file:
        return file.readlines()

def strip_string_list(input_text:list[str])->list[str]:
    return [text.strip() for text in input_text]

file_contents = read_input_file(file_name)
processed_input = strip_string_list(file_contents)

max_red = 12
max_green = 13
max_blue = 14

game_id_possible_list = []
game_possible_count = 0
for play in processed_input:
    split_items = play.split(": ")
    game_id = int(split_items[0].split(" ")[1])

    split_delimiters = r"; "
    rounds = re.split(split_delimiters, split_items[1])

    round_status = []
    for single_round in rounds:
        # count colours in this game round
        green_count = 0
        red_count = 0
        blue_count = 0

        outcomes = single_round.split(", ")
        for item in outcomes:
            value, colour = tuple(item.split(" "))
            value = int(value)
            if colour == "red":
                red_count += value
            elif colour == "green":
                green_count += value
            else:
                blue_count += value

        # check if game was possible
        if red_count > max_red or green_count > max_green or blue_count > max_blue:
            round_status.append(False) # game was impossible
        else:
            round_status.append(True) # game was possible

    if all(round_status):
        game_id_possible_list.append(game_id)
        game_possible_count += game_id

print(f"The sum of game IDs that are possible is {game_possible_count}")


# Part 2

game_id_possible_list = []
game_possible_count = 0
for play in processed_input:
    split_items = play.split(": ")
    game_id = int(split_items[0].split(" ")[1])

    split_delimiters = r"; "
    rounds = re.split(split_delimiters, split_items[1])

    round_status = []
    # maximum color value
    green_count = 0
    red_count = 0
    blue_count = 0

    for single_round in rounds:

        outcomes = single_round.split(", ")
        for item in outcomes:
            value, colour = tuple(item.split(" "))
            value = int(value)
            if colour == "red":
                if value > red_count:
                    red_count = value
            elif colour == "green":
                if value > green_count:
                    green_count = value
            else:
                if value > blue_count:
                    blue_count = value

        # check if game was possible
        if red_count > max_red or green_count > max_green or blue_count > max_blue:
            round_status.append(False) # game was impossible
        else:
            round_status.append(True) # game was possible

    game_power = red_count * green_count * blue_count
    game_possible_count += game_power

print(f"The sum of colour powers is {game_possible_count}")


