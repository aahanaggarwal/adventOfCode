from collections import defaultdict

file = open("inputs/day8.txt", "r")
test_file = open("inputs/day8_test.txt", "r")
# file = test_file

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
        if digit in set_digits[index]:
                continue
        curr = line_mapping[index][digit]
        if len(curr) == 0:
            for i in chars_in_digit:
                line_mapping[index][digit].append(i)
        else:
            line_mapping[index][digit] = list(set(curr) & set(list(chars_in_digit)))

for line_num, input_value in enumerate(input_values):
    for index, string in enumerate(input_value):
        if len(string) in unique_digit_map.keys():
            update_line_map_for_unique(line_num, string, unique_digit_map[len(string)])

    cf_candidates = []
    for digit in line_mapping[line_num]:
        if sorted(line_mapping[line_num][digit]) == ['c', 'f']:
            cf_candidates.append(digit)

    for index, string in enumerate(input_value):
        num_cf_candidates = 0
        f_candidate = ''
        for digit in string:
            if digit in cf_candidates:
                num_cf_candidates += 1
                f_candidate = digit
            
        if num_cf_candidates == 1 and len(string) == 6:
            break

    cf_candidates.remove(f_candidate)
    c_candidate = cf_candidates[0]
    line_mapping[line_num][f_candidate] = 'f'
    line_mapping[line_num][c_candidate] = 'c'
    set_digits[line_num].add(f_candidate)
    set_digits[line_num].add(c_candidate)

    for digit in line_mapping[line_num].keys():
        if type(line_mapping[line_num][digit]) == list:
            if 'f' in line_mapping[line_num][digit]:
                line_mapping[line_num][digit].remove('f')
            if 'c' in line_mapping[line_num][digit]:
                line_mapping[line_num][digit].remove('c')
    
    for digit in line_mapping[line_num].keys():
        if type(line_mapping[line_num][digit]) == list:
            if len(line_mapping[line_num][digit]) == 1:
                line_mapping[line_num][digit] = line_mapping[line_num][digit][0]
                set_digits[line_num].add(digit)

    db_candidates = []
    for digit in line_mapping[line_num]:
        if sorted(line_mapping[line_num][digit]) == ['b', 'd']:
            db_candidates.append(digit)

    for index, string in enumerate(input_value):
        num_db_candidates = 0
        b_candidate = ''
        for digit in string:
            if digit in db_candidates:
                num_db_candidates += 1
                b_candidate = digit
        if num_db_candidates == 1 and len(string) == 6:
            break

    db_candidates.remove(b_candidate)
    d_candidate = db_candidates[0]
    line_mapping[line_num][b_candidate] = 'b'
    line_mapping[line_num][d_candidate] = 'd'
    set_digits[line_num].add(b_candidate)
    set_digits[line_num].add(d_candidate)

    for digit in line_mapping[line_num].keys():
        if type(line_mapping[line_num][digit]) == list:
            if 'd' in line_mapping[line_num][digit]:
                line_mapping[line_num][digit].remove('d')
            if 'b' in line_mapping[line_num][digit]:
                line_mapping[line_num][digit].remove('b')
    
    for digit in line_mapping[line_num].keys():
        if type(line_mapping[line_num][digit]) == list:
            if len(line_mapping[line_num][digit]) == 1:
                line_mapping[line_num][digit] = line_mapping[line_num][digit][0]
                set_digits[line_num].add(digit)


    for set_digit in set_digits[line_num]:
        mapped_to = line_mapping[line_num][set_digit]
        for digit in line_mapping[line_num].keys():
            if type(line_mapping[line_num][digit]) == list:
                if mapped_to in line_mapping[line_num][digit]:
                    line_mapping[line_num][digit].remove(mapped_to)

    eg_candidates = []
    for digit in line_mapping[line_num]:
        if sorted(line_mapping[line_num][digit]) == ['e', 'g']:
            eg_candidates.append(digit)

    print(eg_candidates)
    for index, string in enumerate(input_value):
        num_eg_candidates = 0
        g_candidate = ''
        for digit in string:
            if digit in eg_candidates:
                num_eg_candidates += 1
                g_candidate = digit
        if num_eg_candidates == 1 and len(string) == 6:
            break

    eg_candidates.remove(g_candidate)
    e_candidate = eg_candidates[0]
    line_mapping[line_num][e_candidate] = 'e'
    line_mapping[line_num][g_candidate] = 'g'
    set_digits[line_num].add(g_candidate)
    set_digits[line_num].add(e_candidate)
    
    print(line_mapping[line_num])
    print(set_digits[line_num])

def convert_string_with_mapping(line_num, string):
    curr_map = line_mapping[line_num]
    final_string = []
    for i, char in enumerate(string):
        final_string.append(curr_map[char])

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

total_sum = 0

for line_num, output_value in enumerate(output_values):
    number = 0
    print(line_mapping[line_num])
    for index, string in enumerate(output_value):
        fixed_string = convert_string_with_mapping(line_num, string)
        digit = string_to_digit[fixed_string]
        number = number * 10 + digit
    print(number)
    total_sum += number

for i in range(7):
    print(line_mapping[i])

print(total_sum)
