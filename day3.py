import re
from collections import defaultdict

# create function to read in file
file_name = "day_3_input_test.txt"
#file_name = "day_3_input.txt"
def read_input_file(file_name: str):
    with open(file_name) as file:
        return file.readlines()

def strip_string_list(input_text:list[str])->list[str]:
    return [text.strip() for text in input_text]

file_contents = read_input_file(file_name)
processed_input = strip_string_list(file_contents)

symbol_map = defaultdict(lambda : ".")

# populate symbol map
for row_idx, row in enumerate(processed_input):
    for column_idx, point in enumerate(row):
        if not point.isalnum():
            symbol_map[(row_idx, column_idx)] = point

integer_regex = r"(\d+)"







