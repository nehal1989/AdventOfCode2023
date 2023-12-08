import re

# create function to read in file
file_name = "day_1_input.txt"
def read_input_file(file_name: str):
    with open(file_name) as file:
        return file.readlines()

def strip_string_list(input_text:list[str])->list[str]:
    return [text.strip() for text in input_text]

file_contents = read_input_file(file_name)
processed_input = strip_string_list(file_contents)

### DAY 1 Execution ###

regex = r"(\d)"

int_sum = 0
for item in processed_input:
    matches = re.findall(regex, item)

    if matches:
        calibration_value = int(matches[0]+matches[-1])
        int_sum = int_sum + calibration_value

print(f"The total is {int_sum}")

# Part 2
regex = r"(\d|one|two|three|four|five|six|seven|eight|nine)"

value_map = {
    "one": "1",
    "two": "2",
    "three": "3",
    "four": "4",
    "five": "5",
    "six": "6",
    "seven": "7",
    "eight": "8",
    "nine": "9"
}

int_sum = 0
for item in processed_input:
    matches = re.findall(regex, item)

    first_and_last_values = [matches[0], matches[-1]]

    string_value = ""

    for value in first_and_last_values:
        if value in value_map:
            string_value += value_map[value]
        else:
            string_value += value

    calibration_value = int(string_value)
    int_sum = int_sum + calibration_value

print(f"The total is {int_sum}")