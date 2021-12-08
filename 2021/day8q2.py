from collections import defaultdict

file = open("inputs/day8.txt", "r")
test_file = open("inputs/day8_test.txt", "r")
file = test_file

lines = file.readlines()
output_values = []
input_values = []

for line in lines:
    line = line.strip()
    line = line.split("|")
    input_values.append(line[0].split())
    output_values.append(line[1].split())

unique_digit_map = {
    2: 1,
    4: 4,
    3: 7,
    7: 8
}

line_mapping = defaultdict(lambda: defaultdict(list))
set_digits = []
for i in range(len(lines)):
    set_digits.append(set())

def get_index(a, x):
    for i, y in enumerate(a):
        if x==y:
            return i

    return -1

def update_line_map_for_unique(index, from_str, to_digit):
    chars_in_digit = None

    if to_digit == 1:
        chars_in_digit = 'cf'
    if to_digit == 4:
        chars_in_digit = 'bcdf'
    if to_digit == 7:
        chars_in_digit = 'acf'
    if to_digit == 8:
        chars_in_digit = 'abcdefg'

    for digit in from_str:
        for i in chars_in_digit:
            if digit in set_digits[index]:
                continue
            if i in line_mapping[index][digit]:
                set_digits[index].add(digit)
                line_mapping[index][digit] = [i]
                continue


            line_mapping[index][digit].append(i)
            # if digit in line_mapping[index][1][i] and digit not in line_mapping[index][2]:
            #     line_mapping[index][2].add(digit)
            #     line_mapping[index][1][i] = digit

            # if type(line_mapping[index][1][i]) != list:
            #     continue
            # line_mapping[index][1][i].append(digit)

for line_num, input_value in enumerate(input_values):
    for index, string in enumerate(input_value):
        if len(string) in unique_digit_map.keys():
            update_line_map_for_unique(line_num, string, unique_digit_map[len(string)])

    

    # eight_string = None
    # nine_string = None
    # for index, string in enumerate(input_value):
    #     if len(string) == 7:
    #         eight_string = string
    # for index, string in enumerate(input_value):
    #     num_not_in_set = 0
    #     for character in string:
    #         if character not in line_mapping[line_num][2]:
    #             num_not_in_set += 1
    #     if num_not_in_set == 1 and len(string) == 6:
    #         nine_string = string
    
    # # convert eight_string and nine_string to lists
    # eight_list = list(eight_string)
    # nine_list = list(nine_string)
    # for letter in nine_list:
    #     eight_list.remove(letter)

    # mapped_to_e = eight_list[0]

    # line_mapping[line_num][1][4] = mapped_to_e
    # line_mapping[line_num][2].add(mapped_to_e)

    # all_chars = 'abcdefg'
    # for char in all_chars:
    #     if char not in line_mapping[line_num][2]:
    #         line_mapping[line_num][1][6] = char
    #         line_mapping[line_num][2].add(char)
    #         break

    print(line_mapping[line_num])

def convert_string_with_mapping(line_num, string):
    curr_map = line_mapping[line_num]
    final_string = []
    for i, char in enumerate(string):
        index = get_index(curr_map[1], char)
        final_string.append(curr_map[0][index])

    print(string, "->", "".join(final_string))
    return ''.join(sorted(final_string))

string_to_digit = {
    'abcefg': 0,
    'cf': 1,
    'acdeg': 2,
    'acdfg': 3,
    'bcdf': 4,
    'abdfg': 5,
    'abdefg': 6,
    'acf': 7,
    'abcdefg': 8,
    'abcdfg': 9
}

for line_num, output_value in enumerate(output_values):
    number = 0
    print(line_mapping[line_num])
    for index, string in enumerate(output_value):
        fixed_string = convert_string_with_mapping(line_num, string)
        digit = string_to_digit[fixed_string]
        number = number * 10 + digit
    print(number)

for i in range(7):
    print(line_mapping[i])
